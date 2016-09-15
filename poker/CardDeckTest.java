package enshu4.cardgame.t1165028.card;

import java.util.Iterator;

import junit.framework.TestCase;

public class CardDeckTest extends TestCase {
	private CardDeck deck1 = new CardDeck();

	protected void setUp() throws Exception {
		deck1.addCard(new Card(0,1));   //スペードA
		deck1.addCard(new Card(1,1));   //ダイヤA
		deck1.addCard(new Card(2,1));   //ハートA
		deck1.addCard(new Card(3,1));   //クラブA
		deck1.addCard(new Card(0,1));   //ジョーカー
		super.setUp();
	}

	protected void tearDown() throws Exception {
		super.tearDown();
	}

	public void testCreateFullDeck() {
		CardDeck cardDeck = new CardDeck();    //デッキを生成
		cardDeck.createFullDeck();             //フルデッキにする
		assertEquals(52,cardDeck.size());      //デッキの枚数は52枚のはず
	}

	public void testAddCard() {
		deck1.addCard(new Card(0,2));   //スペード２
		assertEquals("スペード2",deck1.getCardAt(5).toString());   //デッキの一番したのカードはスペード２のはず
	}

	public void testGetCard() {
		assertEquals("スペードA",deck1.getCard().toString());   //デッキの一番上のカードはスペードAのはず
	}

	public void testGetCardAt(int i) {
		assertEquals("ハートA",deck1.getCardAt(3).toString());   //デッキの３番目はハートAのはず
	}

	public void testSearchCardWithIndex() {
		assertEquals(2,deck1.searchCardWithIndex(14));    //ダイヤ２はデッキの２番目にあるはず
	}

	public void testSeeCardAt(int i) {
		assertEquals("クラブA",deck1.seeCardAt(4).toString());   //デッキの４番目はクラブAのはず
	}

	public void testInsertCard() {
		deck1.insertCard(3,new Card(0,3));   //デッキの３番目にスペードの３を挿入
		assertEquals("スペード3",deck1.getCardAt(3).toString());   //デッキの３番目はスペードの３のはず
	}

	public void testIsEmpty() {
		for(int i=0;i<5;i++){                  //カードを取り除いていく
			deck1.getCard();
		}
		assertTrue(deck1.isEmpty());           //デッキは空であるはず
	}

	public void testIterator() {
		Iterator<Card> it = deck1.iterator();   //反復子
		assertTrue(it.hasNext());               //trueがかえってくるはず
	}

	public void testSize() {
		assertEquals(5,deck1.size());    //デッキの枚数は５のはず
	}

}
