package enshu4.cardgame.t1165028.card;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;

/**
 * �J�[�h�f�b�L�N���X
 * @author t1165028
 * @version 1.0, 2013/1/27
 * @since JDK1.5
 *
 */
public class CardDeck {

	/** �J�[�h���X�g */
	private ArrayList<Card> cards = new ArrayList<Card>();
	
	/** �R���X�g���N�^ */
    public CardDeck(){
    	
    }
    
    /** ������t���f�b�L�ɂ��� */
    public void createFullDeck(){
    	System.out.println("==1.�t���f�b�L�����܂�==");
    	for(int i=0;i<=3;i++){
    		for(int j=1;j<=13;j++){
    			Card card = new Card(i,j);
    			cards.add(card);
    		}
    	}
    }
    
    /** �f�b�L���V���b�t������ */
    public void shuffle(){
    	System.out.println("==2.�V���b�t�����܂�==");
    	Collections.shuffle(cards);
    }
    
    /** �f�b�L�̈�ԍŌ�ɁA�C�ӂ̃J�[�h��ǉ����� */
    public void addCard(Card card){
    	cards.add(card);
    }
    
    /** �f�b�L�̈�ԏ�̃J�[�h����� */
    public Card getCard(){
    	Card card = cards.get(0);
    	cards.remove(0);
    	return card;
    }
    
    /** �f�b�L��i�Ԗڂ���A�J�[�h�𔲂���� */
    public Card getCardAt(int i){
    	Card card = cards.get(i);
    	cards.remove(i);
    	return card;
    }
    
    /** �J�[�h�𐮐��\���Ŏw�肷��ƁA���̃J�[�h���f�b�L�̉��Ԗڂɂ��邩�𒲂ׂ� */
    public int searchCardWithIndex(int cardIndex){
    	int i;
    	for(i=0;i<cards.size();i++){
    		if(cardIndex == cards.get(i).toIndex())
    	break;
    	}
    	return (i+1);
    }
    
    /** �f�b�L��i�Ԗڂɂ���J�[�h������ */
    public Card seeCardAt(int i){
    	return cards.get(i);
    }
    
    /** �f�b�L��i�ԖڂɃJ�[�h��}������ */
    public void insertCard(int i,Card card){
    	cards.add(i,card);
    }
    
    /** ���݂̂��ׂẴJ�[�h����ʂɕ\������ */
    public void showAllCards(){
    	System.out.println("-------���݂̎R��\�����܂��B-------");
    	for(int i=1;i<cards.size();i++){
    		System.out.println(i + "�Ԗڂ̃J�[�h�F" + cards.get(i).toString());
    	}
    	System.out.println("-------�����܂�-------");
    }
    
    /** ���݂̃f�b�L���󂩂ǂ����A���肷�� */
    public boolean isEmpty(){
    	return cards.isEmpty();
    }
    
    /** ���݃f�b�L�ɂ���J�[�h���A�O���Ő����グ�\�Ȃ悤�ɁA�����q��Ԃ� */
    public Iterator<Card> iterator(){
    	Iterator<Card> it = cards.iterator();
    	return it;
    }
    
    /** ���݃f�b�L�ɂ���J�[�h������Ԃ� */
    public int size(){
    	return cards.size();
    }
    
    /** ���݃f�b�L�ɂ���J�[�h�̔z��𐶐����ĕԂ� */
    public Card[] toArray(){
    	return (Card[]) cards.toArray();
    }
	
}
