package enshu4.cardgame.t1165028.card;

public class CardComparatorNumber implements java.util.Comparator{

	/** ソートを行うために数字の比較をする */
	public int compare(Object s, Object t){
		return ((Card) s).getNumber() - ((Card) t).getNumber();
	}
	
}
