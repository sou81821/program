package enshu4.cardgame.t1165028.card;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

/**
 * �|�[�J�[�Q�[���N���X
 * @author t1165028
 * @version 1.0, 2013/1/27
 * @since JDK1.5
 */
public class PokerGame {
	private ArrayList<Player> playerList = new ArrayList<Player>();   //�v���[���[���X�g
	
	/** �|�[�J�[�Q�[�����s�� */
	public void playPokerGame()throws IOException{

		CardDeck cardDeck = new CardDeck();    //�f�b�L
		Player[] player = new Player[2];       //�v���[���[
		Judge judge = new Judge();

		String str1 = "YOU";
		String str2 = "CPU";
		
		player[0] = new User(str1);      //���[�U�[
		player[1] = new CPU(str2);       //CPU
		
		playerList.add(player[0]);
		playerList.add(player[1]);

		for(Player v: playerList){
			System.out.println("�V�������[�U" + "�u" + v.getName() + "�v" + "������쐬���܂���");
		}

		System.out.println("===�|�[�J�[���n�߂܂��B===");
		cardDeck.createFullDeck();                   //�t���f�b�L���쐬
		cardDeck.shuffle();                          //�f�b�L���V���b�t��
		System.out.println("�T�����z��܂��B");
		
		for(Player v: playerList){                   //�f�b�L����T������D�ɉ�����
			for(int i=0;i<5;i++){
				v.addCard(cardDeck.getCard());
			}
		}
		
		for(Player v:playerList){    //��D�̃\�[�g���s��
			for(int i=0;i<2;i++){
				v.sort();
			}
		}
		
		System.out.println("���Ȃ��̎�D��\�����܂��B");
		
		for(int i=0;i<5;i++){                       //��D��\��
			System.out.println((i+1) + "." + player[0].seeCardAt(i));
		}
		
		judge.judge(playerList);                    //���ꂼ��̎�D�̖��𔻒�
		
		for(Player v:playerList){
				v.chooseHand(playerList,cardDeck);  //��D������
		}
		
		for(Player v:playerList){                   //��D�̃\�[�g���s��
			for(int i=0;i<2;i++){
				v.sort();
			}
		}
		
		System.out.println("���Ȃ��̎�D��\�����܂��B");
		
		for(int i=0;i<5;i++){                        //����������̎�D��\��
			System.out.println((i+1) + "." + player[0].seeCardAt(i));
		}
		
		System.out.println("�����I�I�I�I�I�I�I");
		
		judge.judge(playerList);                    //���ꂼ��̎�D�̖��𔻒�
		judge.print();                              //���ꂼ��̎�D��\��
		judge.result();                             //���ʂ𔻒�
		
		}

}
