require 'mechanize'
require 'date'
require 'pry'
require 'capybara/poltergeist'

def scraping_crowd(session, today, check_time)
  can_reserve_from_web = false  # web予約可能か
  crowd = false                 # 混んでいるか

  # 店舗名・住所・ジャンル取得
  name = session.all(".rst-name")[0].all("p")[0].text
  address = session.find(".address").all("p")[0].text
  check_time = 1800

  # webからの予約が可能か確認
  begin
    # select = session.find("#rstinfo-booking-visit-time")
    # select = session.all(".js-show-yoyaku-modal-trigger")[0]
    session.all(".js-show-yoyaku-modal-trigger")[0].trigger("click")
    can_reserve_from_web = true

    calender = session.find(".js-week-wrap")
    today_button_class = calender.all("p")[today-1][:class]
    if today_button_class.include?("is-selectable")
      crowd = false
      puts "空いてる"
    else
      crowd = true
      puts "混んでる"
    end

    # 当日の日付ボタンがクリックできるか確認
    # begin
    #   # calender.all("p")[today-1].trigger("click")
    #   if session.all(".js-timelist-items").to_a.length > 0
    #     timelist.each do |time|
    #       if time.find("a").text.gsub(/:/, "").to_i == check_time
    #         binding.pry
    #       else
    #         puts time.find("a").text.gsub(/:/, "").to_i
    #       end
    #     end
    #   else
    #     puts "当日の日付ボタンクリックできません(else)"
    #   end
    # rescue
    #   puts "当日の日付ボタンクリックできません(rescue)"
    # end

    # 当日の日付ボタンがクリックできるか確認
    # begin
    #   # select.select(check_time.slice(0,2) + ":" + check_time.slice(2,4))
    #   # session.find(".js-form-widget-iframe-link").trigger("click")
    #   calender = session.find(".js-week-wrap")
    #   calender.all("p")[today-1].trigger("click")
    #
    #   store_open = true
    #   puts "営業時間内"
    #
    #   # フレーム移動
    #   session.within_frame(session.find(".cboxIframe")) do
    #     # 空席かどうか確認
    #     begin
    #       message = session.find(".booking-modal__result-message").text
    #       crowd = true
    #       print("満室：", message, "\n")
    #     rescue
    #       puts "空室"
    #     end
    #   end
    #
    # rescue
    #   puts "営業時間外"
    # end

  # web予約不可（webから混雑状況確認できない）
  rescue
    puts "web予約不可"
  end

  puts name
  puts address
  print(can_reserve_from_web, crowd, "\n")
  return address, crowd
end

# 食べログから混雑状況をスクレイピング
def scraping_from_tabelog
  # search_url = 'http://tabelog.com/hyogo/A2801/A280101/R4483/rstLst/?vs=1&sa=%E4%B8%89%E5%AE%AE%E9%A7%85%EF%BC%88%E7%A5%9E%E6%88%B8%E5%B8%82%E5%96%B6%EF%BC%89&sk=%25E5%25B1%2585%25E9%2585%2592%25E5%25B1%258B&lid=hd_search1&vac_net=&svd=20160922&svt=1900&svps=2&hfc=1&Cat=RC&LstCat=RC21&LstCatD=RC2101&sw='
  search_url = 'https://tabelog.com/hyogo/A2801/A280108/R10646/rstLst/?vs=1&sa=%E5%85%AD%E7%94%B2%E9%A7%85&sk=%25E5%25B1%2585%25E9%2585%2592%25E5%25B1%258B&lid=hd_search1&vac_net=&svd=20161021&svt=1900&svps=2&hfc=1&Cat=RC&LstCat=RC21&LstCatD=RC2101&cat_sk=%E5%B1%85%E9%85%92%E5%B1%8B'

  Capybara.register_driver :poltergeist do |app|
    Capybara::Poltergeist::Driver.new(app, {:js_errors => false, :timeout => 1000})
  end
  session = Capybara::Session.new(:poltergeist)
  page_count = 1

  # 現在時刻取得
  today = Time.now.day
  now = Time.now
  if now.min >= 30
    check_time = (now.hour+1).to_s + "00"
  else
    check_time = now.hour.to_s + "30"
  end
  puts check_time

  while true
    session.visit search_url
    stores = session.all(".list-rst__rst-name-target")
    store_urls = []
    stores.each do |store|
      store_urls << store[:href]
    end

    # 各店舗の混雑状況を確認（ web予約可能か確認 -> 営業時間内か確認 -> 空室か確認 ）
    for i in 0..(store_urls.length-1) do
      puts "----------------------------------"
      puts store_urls[i]
      sleep(1)
      session.visit store_urls[i]
      address, crowd = scraping_crowd(session, today, check_time)
    end

    # 次ページへのリンクに移動
    is_last_page = true
    page_count += 1
    session.visit search_url
    pagenation = session.find(".page-move__num").all("a")
    pagenation.each do |page|
      if page.text.to_i == page_count
        search_url = page[:href]
        puts "---------------------"
        puts search_url
        puts "---------------------"
        session.visit search_url
        is_last_page = false
        break
      end
    end
    # 次のページがなければ終了
    if is_last_page == true
      break
    end
  end

  # web予約可能ならデータベースに格納
  # [ユーザID(0), 時刻，店舗名，住所，営業時間内か，混雑状況]
end

# hotpepperグルメから混雑状況をスクレイピング
def scraping_from_hotpepper
  url = "https://www.hotpepper.jp/CSP/psh010/doBasic?FWT=%E4%B8%89%E5%AE%AE%E3%80%80%E5%B1%85%E9%85%92%E5%B1%8B&SA=SA24"
  agent = Mechanize.new
  html = agent.get(url)
  elements = html.search('.shopDetailTop')
  elements.each do |element|
    puts element.search('.calendarContainer')
  end
end

scraping_from_tabelog
