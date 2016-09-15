package enshu4.cardgame.t1165028.card;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

/**
 * ポーカーゲームクラス
 * @author t1165028
 * @version 1.0, 2013/1/27
 * @since JDK1.5
 */
public class PokerGame {
	private ArrayList<Player> playerList = new ArrayList<Player>();   //プレーヤーリスト
	
	/** ポーカーゲームを行う */
	public void playPokerGame()throws IOException{

		CardDeck cardDeck = new CardDeck();    //デッキ
		Player[] player = new Player[2];       //プレーヤー
		Judge judge = new Judge();

		String str1 = "YOU";
		String str2 = "CPU";
		
		player[0] = new User(str1);      //ユーザー
		player[1] = new CPU(str2);       //CPU
		
		playerList.add(player[0]);
		playerList.add(player[1]);

		for(Player v: playerList){
			System.out.println("新しいユーザ" + "「" + v.getName() + "」" + "さんを作成しました");
		}

		System.out.println("===ポーカーを始めます。===");
		cardDeck.createFullDeck();                   //フルデッキを作成
		cardDeck.shuffle();                          //デッキをシャッフル
		System.out.println("５枚ずつ配ります。");
		
		for(Player v: playerList){                   //デッキから５枚ずつ手札に加える
			for(int i=0;i<5;i++){
				v.addCard(cardDeck.getCard());
			}
		}
		
		for(Player v:playerList){    //手札のソートを行う
			for(int i=0;i<2;i++){
				v.sort();
			}
		}
		
		System.out.println("あなたの手札を表示します。");
		
		for(int i=0;i<5;i++){                       //手札を表示
			System.out.println((i+1) + "." + player[0].seeCardAt(i));
		}
		
		judge.judge(playerList);                    //それぞれの手札の役を判定
		
		for(Player v:playerList){
				v.chooseHand(playerList,cardDeck);  //手札を交換
		}
		
		for(Player v:playerList){                   //手札のソートを行う
			for(int i=0;i<2;i++){
				v.sort();
			}
		}
		
		System.out.println("あなたの手札を表示します。");
		
		for(int i=0;i<5;i++){                        //交換した後の手札を表示
			System.out.println((i+1) + "." + player[0].seeCardAt(i));
		}
		
		System.out.println("勝負！！！！！！！");
		
		judge.judge(playerList);                    //それぞれの手札の役を判定
		judge.print();                              //それぞれの手札を表示
		judge.result();                             //結果を判定
		
		}

}
