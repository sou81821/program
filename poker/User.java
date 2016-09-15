package enshu4.cardgame.t1165028.card;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class User extends Player{
	public User(String name){
		super(name);    //Player�̖��O���R���X�g���N�^�ɂ킽��
	}
	
	public void chooseHand(ArrayList<Player> playerList, CardDeck cardDeck) throws IOException{
		
		Player [] p = playerList.toArray(new Player [2]);
		System.out.println("�J�[�h���������܂��B");
		System.out.println("��������J�[�h���A�J�[�h�Ɋ��蓖�Ă��Ă��鐔�����傫�����ɁA�R���}��؂�ɓ��͂��Ă��������B");  //�J�[�h�Ɋ��蓖�Ă��Ă��鐔�����傫�����Ɍ�������J�[�h���w�肳����
		BufferedReader br =
				new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		
		String[] a = str.split(",");     //�w�肵���������R���}��؂�Ŕz��ɓ���
		for(int i=0;i<a.length;i++){     //�w�肵���J�[�h���폜����
			p[0].cardRemove(Integer.parseInt(a[i]));
		}
	
		while(p[0].size() < 5){    //��D���T���ɂȂ�܂Ńf�b�L����J�[�h���[
			p[0].addCard(cardDeck.getCard());
		}
	}
	
}
