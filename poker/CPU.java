package enshu4.cardgame.t1165028.card;

import java.io.IOException;
import java.util.ArrayList;

public class CPU extends Player{
	public CPU(String name){
		super(name);    //CPU�̖��O���R���X�g���N�^�ɂ킽��
	}
	
	public void chooseHand(ArrayList<Player> playerList, CardDeck cardDeck)throws IOException{
		Player [] p = playerList.toArray(new Player [2]);
		Judge judge = new Judge();
		
		if(judge.getBResult() == 0){           //�����m�[�y�A�Ȃ�
			for(int i=0;i<5;i++){              //�J�[�h��S�ւ�
				p[1].cardRemove(1);
			}
			while(p[1].size() < 5){            //��D���T���ɂȂ�܂Ńf�b�L����J�[�h���[
				p[1].addCard(cardDeck.getCard());
			}
		}
		
	}
}
