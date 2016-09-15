package enshu4.cardgame.t1165028.card;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

/**
 * プレーヤークラス
 * @author t1165028
 * @version 1.0, 2013/1/27
 * @since JDK1.5
 */
public abstract class Player {
	
	private ArrayList<Card> cardList = new ArrayList<Card>();   //手札リスト
	
	/** プレイヤー名 */
	private String name;
	
	/** プレーヤークラスのコンストラクタ */
	public Player(String name) {
		super();
		this.name = name;
	}
	
	/** 手札を選ぶ */
	public abstract void chooseHand(ArrayList<Player> playerList, CardDeck cardDeck)throws IOException;     //抽象メソッド
	
	/** 手札をカードの数字が昇順になるようにソートする */
	public void sort(){
		Collections.sort(cardList, new CardComparatorNumber());
	}
	
	/** デッキのi番目のカードの数字を取得する */
	public int getCardNumber(int i){
		Card card = cardList.get(i);
    	return card.getNumber();
	}
	
	/** デッキのi番目のカードの絵柄を取得する */
	public int getCardSuit(int i){
		Card card = cardList.get(i);
    	return card.getSuit();
	}
	
	/** デッキのi番目から、カードを抜き取る */
    public Card getCardAt(int i){
    	Card card = cardList.get(i);
    	cardList.remove(i);
    	return card;
    }
	
    /** 手札にカードを加える */
	public void addCard(Card card){
		cardList.add(card);
	}
	
	/** 手札のi番目のカードを見る */
	public Card seeCardAt(int i){
		return cardList.get(i);
	}
	
	/** 手札のi番目のカードを削除する */
	public void cardRemove(int i){
		cardList.remove(i-1);
	}
	
	 /** 現在デッキにあるカード枚数を返す */
    public int size(){
    	return cardList.size();
    }
	
	/** プレーヤー名を取得させる */
	public String getName(){
		return name;
	}
	
}