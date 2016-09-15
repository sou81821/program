package enshu4.cardgame.t1165028.card;

import junit.framework.TestCase;

public class PlayerTest extends TestCase {
	private Player player = new User("Taro");
	
	protected void setUp() throws Exception {
		player.addCard(new Card(0,1));   //スペードA
		player.addCard(new Card(1,3));   //ダイヤ3
		player.addCard(new Card(2,1));   //ハートA
		player.addCard(new Card(3,1));   //クラブA
		super.setUp();
	}

	protected void tearDown() throws Exception {
		super.tearDown();
	}

	public void testSort() {
		player.sort();
		assertEquals("ダイヤ3",player.seeCardAt(3).toString());
	}

	public void testGetCardNumber(int i) {
		assertEquals(1,player.getCardNumber(3));
	}

	public void testGetCardSuit(int i) {
		assertEquals(2,player.getCardSuit(3));
	}

	public void testGetCardAt(int i) {
		assertEquals("クラブA",player.getCardAt(4).toString());
	}

	public void testAddCard() {
		player.addCard(new Card(0,5));  //スペード5
		assertEquals("スペード5",player.getCardAt(4).toString());
	}

	public void testSeeCardAt() {
		assertEquals("クラブA",player.seeCardAt(3).toString());
	}

	public void testCardRemove() {
		player.cardRemove(2);
		assertEquals("ハートA",player.getCardAt(1).toString());
	}

	public void testSize() {
		assertEquals(4,player.size());
	}

	public void testGetName() {
		assertEquals("Taro",player.getName());
	}

}
