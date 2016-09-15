package enshu4.cardgame.t1165028.card;

import java.util.ArrayList;

/**
 * �J�[�h�N���X
 * @author t1165028
 * @version 1.0, 2013/1/27
 * @since JDK1.5
 */
public class Card {
	
	/**
	 *  �G�� 0�i�X�y�[�h�j, 1�i�_�C���j, 2�i�n�[�g�j, 3�i�N���u�j
	 */
	private int suit;
	/** ���� */
	private int number;
	
	/** �R���X�g���N�^ */
	public Card(int suit,int number){
		super();
		this.suit = suit;
		this.number = number;
	}
    
	/** �G�����O������擾���� */
	public int getSuit(){
		return suit;
	}
	
	/** �������O������擾���� */
	public int getNumber(){
		return number;
	}
	
	/** �J�[�h���𐮐��\���ɕϊ����� */
	public int toIndex(){
		return(getIndex(suit,number));
	}
	
	/** �J�[�h���𕶎���\���ɕϊ����� */
	public String toString(){
		String stringSuit = "";
		String stringNumber = "";
		
		switch(suit){
		case -1:
			stringSuit = "�W���[�J�[";
			break;
		case 0:
			stringSuit = "�X�y�[�h";
			break;
		case 1:
			stringSuit = "�_�C��";
			break;
		case 2:
			stringSuit = "�n�[�g";
			break;
		case 3:
			stringSuit = "�N���u";
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
	
	/** �J�[�h������ʂɏo�͂��� */
	public void show(){
		System.out.println(toString());
	}
	
	/** �G��(0-3)�Ɛ���(1-13)��^����ƁA�Ή�����J�[�h�̐����\����Ԃ� */
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
