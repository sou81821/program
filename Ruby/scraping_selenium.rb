require 'selenium-webdriver'
require 'mechanize'
require 'date'
require 'pry'

# 食べログから混雑状況をスクレイピング
def scraping_from_tabelog
  search_url = 'http://tabelog.com/hyogo/A2801/A280101/R4483/rstLst/?vs=1&sa=%E4%B8%89%E5%AE%AE%E9%A7%85%EF%BC%88%E7%A5%9E%E6%88%B8%E5%B8%82%E5%96%B6%EF%BC%89&sk=%25E5%25B1%2585%25E9%2585%2592%25E5%25B1%258B&lid=hd_search1&vac_net=&svd=20160922&svt=1900&svps=2&hfc=1&Cat=RC&LstCat=RC21&LstCatD=RC2101&sw='
  agent = Mechanize.new
  html = agent.get(search_url)
  stores = html.search(".list-rst__rst-name-target")
  store_urls = []
  stores.each do |store|
    store_urls << store[:href]
  end
  driver = Selenium::WebDriver.for :chrome

  for i in 0..(store_urls.length-1) do
    sleep(1)
    driver.navigate.to store_urls[i]

    # 現在時刻取得
    now = Time.now
    if now.min >= 30
      check_time = (now.hour+1).to_s + "00"
    else
      check_time = now.hour.to_s + "30"
    end
    puts check_time

    # 住所取得
    address = driver.find_element(:class, "address").find_elements(:tag_name, "p")[0].text
    puts address

    # webからの予約可能な店舗なら「空席確認ボタン」クリック
    begin
      select = Selenium::WebDriver::Support::Select.new(driver.find_element(:id, "rstinfo-booking-visit-time"))
      begin
        select.select_by(:value, check_time)
        driver.find_element(:class, "js-form-widget-iframe-link").click

        # モーダルフレームに移動
        driver.switch_to.frame(driver.find_element(:class, "cboxIframe"))

        # 空いていない旨のメッセージ確認
        begin
          message = driver.find_element(:class, "booking-modal__result-message").text
        rescue
          message = ""
        end
        store_open = true
        puts message
        puts message.empty?
      rescue
        store_open = false
      end
      can_reserve = true
    rescue
      can_reserve = false
    end

    puts can_reserve
    puts store_open
  end

  driver.quit

  # データベースに格納
  #[時刻，住所，営業時間内か，空席あるか]
end

# hotpepperグルメから混雑状況をスクレイピング
def scraping_from_hotpepper
  url = "https://www.hotpepper.jp/CSP/psh010/doBasic?FWT=%E4%B8%89%E5%AE%AE%E3%80%80%E5%B1%85%E9%85%92%E5%B1%8B&SA=SA24"
  agent = Mechanize.new
  html = agent.get(url)
  elements = html.search('.shopDetailTop')
  elements.each do |element|
    binding.pry
    puts element.search('.calendarContainer')
  end
end

def main
  scraping_from_tabelog
  #scraping_from_hotpepper
end

main
