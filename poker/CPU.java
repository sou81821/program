package enshu4.cardgame.t1165028.card;

import java.io.IOException;
import java.util.ArrayList;

public class CPU extends Player{
	public CPU(String name){
		super(name);    //CPUの名前つきコンストラクタにわたす
	}
	
	public void chooseHand(ArrayList<Player> playerList, CardDeck cardDeck)throws IOException{
		Player [] p = playerList.toArray(new Player [2]);
		Judge judge = new Judge();
		
		if(judge.getBResult() == 0){           //もしノーペアなら
			for(int i=0;i<5;i++){              //カードを全替え
				p[1].cardRemove(1);
			}
			while(p[1].size() < 5){            //手札が５枚になるまでデッキからカードを補充
				p[1].addCard(cardDeck.getCard());
			}
		}
		
	}
}
