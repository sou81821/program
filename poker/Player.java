package enshu4.cardgame.t1165028.card;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

/**
 * �v���[���[�N���X
 * @author t1165028
 * @version 1.0, 2013/1/27
 * @since JDK1.5
 */
public abstract class Player {
	
	private ArrayList<Card> cardList = new ArrayList<Card>();   //��D���X�g
	
	/** �v���C���[�� */
	private String name;
	
	/** �v���[���[�N���X�̃R���X�g���N�^ */
	public Player(String name) {
		super();
		this.name = name;
	}
	
	/** ��D��I�� */
	public abstract void chooseHand(ArrayList<Player> playerList, CardDeck cardDeck)throws IOException;     //���ۃ��\�b�h
	
	/** ��D���J�[�h�̐����������ɂȂ�悤�Ƀ\�[�g���� */
	public void sort(){
		Collections.sort(cardList, new CardComparatorNumber());
	}
	
	/** �f�b�L��i�Ԗڂ̃J�[�h�̐������擾���� */
	public int getCardNumber(int i){
		Card card = cardList.get(i);
    	return card.getNumber();
	}
	
	/** �f�b�L��i�Ԗڂ̃J�[�h�̊G�����擾���� */
	public int getCardSuit(int i){
		Card card = cardList.get(i);
    	return card.getSuit();
	}
	
	/** �f�b�L��i�Ԗڂ���A�J�[�h�𔲂���� */
    public Card getCardAt(int i){
    	Card card = cardList.get(i);
    	cardList.remove(i);
    	return card;
    }
	
    /** ��D�ɃJ�[�h�������� */
	public void addCard(Card card){
		cardList.add(card);
	}
	
	/** ��D��i�Ԗڂ̃J�[�h������ */
	public Card seeCardAt(int i){
		return cardList.get(i);
	}
	
	/** ��D��i�Ԗڂ̃J�[�h���폜���� */
	public void cardRemove(int i){
		cardList.remove(i-1);
	}
	
	 /** ���݃f�b�L�ɂ���J�[�h������Ԃ� */
    public int size(){
    	return cardList.size();
    }
	
	/** �v���[���[�����擾������ */
	public String getName(){
		return name;
	}
	
}