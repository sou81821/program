package enshu4.cardgame.t1165028.card;

import java.util.ArrayList;

/**
 * 判定クラス
 * @author t1165028
 * @version 1.0, 2013/1/27
 * @since JDK1.5
 */
public class Judge {

	private int aResult, bResult;           //プレーヤーの手札の判定結果
	
	/** ユーザーの手札の判定結果を返す */
	public int getAResult(){
		return this.aResult;
	}
	
	/** CPUの手札の判定結果を返す */
	public int getBResult(){
		return this.bResult;
	}
	
	/** コンストラクタ */
	public Judge(){
		aResult = 0;
		bResult = 0;
	}
	
	/** 手札の役を判定する */
	public void judge(ArrayList<Player> playerList){
		Player [] p = playerList.toArray(new Player [2]);
		
		int [] aNumber = new int[5];   //ユーザーのカードの数字を格納しておく配列
		int [] bNumber = new int[5];   //CPUのカードの数字を格納しておく配列
		int [] aSuit = new int[5];     //ユーザーのカードの絵柄を格納しておく配列
		int [] bSuit = new int[5];     //CPUのカードの絵柄を格納しておく配列
		
		int aNumberOfPair = 0, bNumberOfPair = 0;          //ペアの数
		
		/* 0 : ノーペア
		 * 1 : １ペア
		 * 2 : ２ペア
		 * 3 : ３カード
		 * 4 : ストレート
		 * 5 : フラッシュ
		 * 6 : フルハウス
		 * 7 : ４カード
		 * 8 : ストレートフラッシュ
		 * 9 : ロイヤルストレートフラッシュ
		 */
		
		
		for(int i=0;i<5;i++){
			aNumber[i] = p[0].getCardNumber(i);
			aSuit[i] = p[0].getCardSuit(i);
		}
		
		for(int i=0;i<5;i++){
			bNumber[i] = p[1].getCardNumber(i);
			bSuit[i] = p[1].getCardSuit(i);
		}
		
		//ユーザーの役判定
		//ノーペアの判定
		if(aNumber[0] != aNumber[1] && aNumber[1] != aNumber[2] && aNumber[2] != aNumber[3] && aNumber[3] != aNumber[4]){
			aResult = 0;
		}
		
		//フラッシュの判定
		if(aSuit[0] == aSuit[1] && aSuit[0] == aSuit[2] && aSuit[0] == aSuit[3] && aSuit[0] == aSuit[4]){
			aResult = 5;
		}
		
		//ストレートの判定
		if(aNumber[4]==aNumber[3]+1 && aNumber[3]==aNumber[2]+1 && aNumber[2]==aNumber[1]+1 && aNumber[1]==aNumber[0]+1){
			aResult = 4;
		}
		//ストレートフラッシュの判定
		else if(aNumber[4]==aNumber[3]+1 && aNumber[3]==aNumber[2]+1 && aNumber[2]==aNumber[1]+1 && aNumber[1]==aNumber[0]+1 && aNumber[1]!=aNumber[0]+9){
			aResult = 8;
		}
		//ロイヤルストレートフラッシュの判定
		else if(aNumber[0]==1 && aNumber[1]==10 && aNumber[2]==11 && aNumber[3]==12 && aNumber[4]==13 && aSuit[0]==aSuit[1] && aSuit[1]==aSuit[2] && aSuit[2]==aSuit[3] && aSuit[3]==aSuit[4]){
			aResult = 9;
		}
		
		//フルハウスの判定
		if(((aNumber[0]==aNumber[1]) && (aNumber[2]==aNumber[3] && aNumber[2]==aNumber[4])) ||
				((aNumber[0]==aNumber[1] && aNumber[0]==aNumber[2]) && (aNumber[3]==aNumber[4]))){
			aResult = 6;
		}
		
		//4カードの判定
		if((aNumber[0]==aNumber[1] && aNumber[0]==aNumber[2] && aNumber[0]==aNumber[3]) ||
				(aNumber[1]==aNumber[2] && aNumber[1]==aNumber[3] && aNumber[1]==aNumber[4])){
			aResult = 7;
		}
		
		//3カードの判定
		if(aResult != 7 && aResult != 6){
			for(int i=2;i<5;i++){
				if(aNumber[i-2]==aNumber[i-1] && aNumber[i-1]==aNumber[i]){
					aResult = 3;
				}
			}
		}
		
		//１ペア、２ペアの判定
		if(aResult!=7 && aResult!=3){     //３カードでも４カードでもなかったら
			for(int i=0;i<4;i++){	
				if(aNumber[i]==aNumber[i+1]){
					aNumberOfPair++;
				}
			}
		}
		if(aNumberOfPair==1)
			aResult = 1;
		else if(aNumberOfPair==2)
			aResult = 2;
		
		
		//CPUの役判定
		//ノーペアの判定
		if(bNumber[0] != bNumber[1] && bNumber[1] != bNumber[2] && bNumber[2] != bNumber[3] && bNumber[3] != bNumber[4]){
			bResult = 0;
		}
		
		//フラッシュの判定
		if(bSuit[0] == bSuit[1] && bSuit[0] == bSuit[2] && bSuit[0] == bSuit[3] && bSuit[0] == bSuit[4]){
			bResult = 5;
		}
		
		//ストレートの判定
		if(bNumber[4]==bNumber[3]+1 && bNumber[3]==bNumber[2]+1 && bNumber[2]==bNumber[1]+1 && bNumber[1]==bNumber[0]+1){
			bResult = 4;
		}
		//ストレートフラッシュの判定
		else if(bNumber[4]==bNumber[3]+1 && bNumber[3]==bNumber[2]+1 && bNumber[2]==bNumber[1]+1 && bNumber[1]==bNumber[0]+1 && bNumber[1]!=bNumber[0]+9){
			bResult = 8;
		}
		//ロイヤルストレートフラッシュの判定
		else if(bNumber[0]==1 && bNumber[1]==10 && bNumber[2]==11 && bNumber[3]==12 && bNumber[4]==13 && bSuit[0]==bSuit[1] && bSuit[1]==bSuit[2] && bSuit[2]==bSuit[3] && bSuit[3]==bSuit[4]){
			bResult = 9;
		}
		
		//フルハウスの判定
		if(((bNumber[0]==bNumber[1]) && (bNumber[2]==bNumber[3] && bNumber[2]==bNumber[4])) ||
				((bNumber[0]==bNumber[1] && bNumber[0]==bNumber[2]) && (bNumber[3]==bNumber[4]))){
			bResult = 6;
		}
		
		//4カードの判定
		if((bNumber[0]==bNumber[1] && bNumber[0]==bNumber[2] && bNumber[0]==bNumber[3]) ||
				(bNumber[1]==bNumber[2] && bNumber[1]==bNumber[3] && bNumber[1]==bNumber[4])){
			bResult = 7;
		}
		
		//3カードの判定
		if(bResult != 7 && bResult != 6){
			for(int i=2;i<5;i++){
				if(bNumber[i-2]==bNumber[i-1] && bNumber[i-1]==bNumber[i]){
					bResult = 3;
				}
			}
		}
		
		//１ペア、２ペアの判定
		if(bResult!=7 && bResult!=3){     //３カードでも４カードでもなかったら
			for(int i=0;i<4;i++){	
				if(bNumber[i]==bNumber[i+1]){
					bNumberOfPair++;
				}
			}
		}
		if(bNumberOfPair==1)
			bResult = 1;
		else if(bNumberOfPair==2)
			bResult = 2;
		
	}
		
				
	
	/** 手札の役を表示する */
	public void print(){
		switch(aResult){
		case 0:
			System.out.println("あなたの手札は「ノーペア」です。");
			break;
		case 1:
			System.out.println("あなたの手札は「１ペア」です。");
			break;
		case 2:
			System.out.println("あなたの手札は「２ペア」です。");
			break;
		case 3:
			System.out.println("あなたの手札は「３カード」です。");
			break;
		case 4:
			System.out.println("あなたの手札は「ストレート」です。");
			break;
		case 5:
			System.out.println("あなたの手札は「フラッシュ」です。");
			break;
		case 6:
			System.out.println("あなたの手札は「フルハウス」です。");
			break;
		case 7:
			System.out.println("あなたの手札は「４カード」です。");
			break;
		case 8:
			System.out.println("あなたの手札は「ストレートフラッシュ」です。");
			break;
		case 9:
			System.out.println("あなたの手札は「ロイヤルストレートフラッシュ」です。");
			break;
		}
		
		switch(bResult){       //CPUの手札の役を表示
		case 0:
			System.out.println("CPUの手札は「ノーペア」です。");
			break;
		case 1:
			System.out.println("CPUの手札は「１ペア」です。");
			break;
		case 2:
			System.out.println("CPUの手札は「２ペア」です。");
			break;
		case 3:
			System.out.println("CPUの手札は「３カード」です。");
			break;
		case 4:
			System.out.println("CPUの手札は「ストレート」です。");
			break;
		case 5:
			System.out.println("CPUの手札は「フラッシュ」です。");
			break;
		case 6:
			System.out.println("CPUの手札は「フルハウス」です。");
			break;
		case 7:
			System.out.println("CPUの手札は「４カード」です。");
			break;
		case 8:
			System.out.println("CPUの手札は「ストレートフラッシュ」です。");
			break;
		case 9:
			System.out.println("CPUの手札は「ロイヤルストレートフラッシュ」です。");
			break;
		}
	}
	
	
	
	
	/** 結果を表示する */
	public void result(){
		if(aResult < bResult)    //勝敗を表示
			System.out.println("あなたの負けです。");
		else if(aResult > bResult)
			System.out.println("あなたの勝ちです。");
		else if(aResult == bResult)
			System.out.println("引き分けです。");
	}
	
}
