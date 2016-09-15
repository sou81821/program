package enshu4.cardgame.t1165028.card;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;

/**
 * カードデッキクラス
 * @author t1165028
 * @version 1.0, 2013/1/27
 * @since JDK1.5
 *
 */
public class CardDeck {

	/** カードリスト */
	private ArrayList<Card> cards = new ArrayList<Card>();
	
	/** コンストラクタ */
    public CardDeck(){
    	
    }
    
    /** 自らをフルデッキにする */
    public void createFullDeck(){
    	System.out.println("==1.フルデッキを作ります==");
    	for(int i=0;i<=3;i++){
    		for(int j=1;j<=13;j++){
    			Card card = new Card(i,j);
    			cards.add(card);
    		}
    	}
    }
    
    /** デッキをシャッフルする */
    public void shuffle(){
    	System.out.println("==2.シャッフルします==");
    	Collections.shuffle(cards);
    }
    
    /** デッキの一番最後に、任意のカードを追加する */
    public void addCard(Card card){
    	cards.add(card);
    }
    
    /** デッキの一番上のカードを取る */
    public Card getCard(){
    	Card card = cards.get(0);
    	cards.remove(0);
    	return card;
    }
    
    /** デッキのi番目から、カードを抜き取る */
    public Card getCardAt(int i){
    	Card card = cards.get(i);
    	cards.remove(i);
    	return card;
    }
    
    /** カードを整数表現で指定すると、そのカードがデッキの何番目にあるかを調べる */
    public int searchCardWithIndex(int cardIndex){
    	int i;
    	for(i=0;i<cards.size();i++){
    		if(cardIndex == cards.get(i).toIndex())
    	break;
    	}
    	return (i+1);
    }
    
    /** デッキのi番目にあるカードを見る */
    public Card seeCardAt(int i){
    	return cards.get(i);
    }
    
    /** デッキのi番目にカードを挿入する */
    public void insertCard(int i,Card card){
    	cards.add(i,card);
    }
    
    /** 現在のすべてのカードを画面に表示する */
    public void showAllCards(){
    	System.out.println("-------現在の山を表示します。-------");
    	for(int i=1;i<cards.size();i++){
    		System.out.println(i + "番目のカード：" + cards.get(i).toString());
    	}
    	System.out.println("-------ここまで-------");
    }
    
    /** 現在のデッキが空かどうか、判定する */
    public boolean isEmpty(){
    	return cards.isEmpty();
    }
    
    /** 現在デッキにあるカードを、外部で数え上げ可能なように、反復子を返す */
    public Iterator<Card> iterator(){
    	Iterator<Card> it = cards.iterator();
    	return it;
    }
    
    /** 現在デッキにあるカード枚数を返す */
    public int size(){
    	return cards.size();
    }
    
    /** 現在デッキにあるカードの配列を生成して返す */
    public Card[] toArray(){
    	return (Card[]) cards.toArray();
    }
	
}
