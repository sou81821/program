package enshu4.cardgame.t1165028.card;

import java.util.ArrayList;

/**
 * カードクラス
 * @author t1165028
 * @version 1.0, 2013/1/27
 * @since JDK1.5
 */
public class Card {
	
	/**
	 *  絵柄 0（スペード）, 1（ダイヤ）, 2（ハート）, 3（クラブ）
	 */
	private int suit;
	/** 数字 */
	private int number;
	
	/** コンストラクタ */
	public Card(int suit,int number){
		super();
		this.suit = suit;
		this.number = number;
	}
    
	/** 絵柄を外部から取得する */
	public int getSuit(){
		return suit;
	}
	
	/** 数字を外部から取得する */
	public int getNumber(){
		return number;
	}
	
	/** カード情報を整数表現に変換する */
	public int toIndex(){
		return(getIndex(suit,number));
	}
	
	/** カード情報を文字列表現に変換する */
	public String toString(){
		String stringSuit = "";
		String stringNumber = "";
		
		switch(suit){
		case -1:
			stringSuit = "ジョーカー";
			break;
		case 0:
			stringSuit = "スペード";
			break;
		case 1:
			stringSuit = "ダイヤ";
			break;
		case 2:
			stringSuit = "ハート";
			break;
		case 3:
			stringSuit = "クラブ";
			break;
		}
		
		
		switch(number){
		case 1:
			stringNumber = "A";
			break;
		case 2:
			stringNumber = "2";
			break;
		case 3:
			stringNumber = "3";
			break;
		case 4:
			stringNumber = "4";
			break;
		case 5:
			stringNumber = "5";
			break;
		case 6:
			stringNumber = "6";
			break;
		case 7:
			stringNumber = "7";
			break;
		case 8:
			stringNumber = "8";
			break;
		case 9:
			stringNumber = "9";
			break;
		case 10:
			stringNumber = "10";
			break;
		case 11:
			stringNumber = "J";
			break;
		case 12:
			stringNumber = "Q";
			break;
		case 13:
			stringNumber = "K";
			break;
		}
		
		return (stringSuit + stringNumber);
		
	}
	
	/** カード情報を画面に出力する */
	public void show(){
		System.out.println(toString());
	}
	
	/** 絵柄(0-3)と数字(1-13)を与えると、対応するカードの整数表現を返す */
	public static int getIndex(int suit,int number){
		int index = 0;
		if(suit == 0)
			index = number;
		else if(suit == 1)
			index = number + 13;
		else if(suit == 2)
			index = number + 26;
		else if(suit == 3)
			index = number + 39;
		
		return index;
	}
	
}
