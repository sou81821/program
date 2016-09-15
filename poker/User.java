package enshu4.cardgame.t1165028.card;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class User extends Player{
	public User(String name){
		super(name);    //Playerの名前つきコンストラクタにわたす
	}
	
	public void chooseHand(ArrayList<Player> playerList, CardDeck cardDeck) throws IOException{
		
		Player [] p = playerList.toArray(new Player [2]);
		System.out.println("カードを交換します。");
		System.out.println("交換するカードを、カードに割り当てられている数字が大きい順に、コンマ区切りに入力してください。");  //カードに割り当てられている数字が大きい順に交換するカードを指定させる
		BufferedReader br =
				new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		
		String[] a = str.split(",");     //指定した数字をコンマ区切りで配列に入力
		for(int i=0;i<a.length;i++){     //指定したカードを削除する
			p[0].cardRemove(Integer.parseInt(a[i]));
		}
	
		while(p[0].size() < 5){    //手札が５枚になるまでデッキからカードを補充
			p[0].addCard(cardDeck.getCard());
		}
	}
	
}
