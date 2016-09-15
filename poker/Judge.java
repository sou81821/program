package enshu4.cardgame.t1165028.card;

import java.util.ArrayList;

/**
 * ����N���X
 * @author t1165028
 * @version 1.0, 2013/1/27
 * @since JDK1.5
 */
public class Judge {

	private int aResult, bResult;           //�v���[���[�̎�D�̔��茋��
	
	/** ���[�U�[�̎�D�̔��茋�ʂ�Ԃ� */
	public int getAResult(){
		return this.aResult;
	}
	
	/** CPU�̎�D�̔��茋�ʂ�Ԃ� */
	public int getBResult(){
		return this.bResult;
	}
	
	/** �R���X�g���N�^ */
	public Judge(){
		aResult = 0;
		bResult = 0;
	}
	
	/** ��D�̖��𔻒肷�� */
	public void judge(ArrayList<Player> playerList){
		Player [] p = playerList.toArray(new Player [2]);
		
		int [] aNumber = new int[5];   //���[�U�[�̃J�[�h�̐������i�[���Ă����z��
		int [] bNumber = new int[5];   //CPU�̃J�[�h�̐������i�[���Ă����z��
		int [] aSuit = new int[5];     //���[�U�[�̃J�[�h�̊G�����i�[���Ă����z��
		int [] bSuit = new int[5];     //CPU�̃J�[�h�̊G�����i�[���Ă����z��
		
		int aNumberOfPair = 0, bNumberOfPair = 0;          //�y�A�̐�
		
		/* 0 : �m�[�y�A
		 * 1 : �P�y�A
		 * 2 : �Q�y�A
		 * 3 : �R�J�[�h
		 * 4 : �X�g���[�g
		 * 5 : �t���b�V��
		 * 6 : �t���n�E�X
		 * 7 : �S�J�[�h
		 * 8 : �X�g���[�g�t���b�V��
		 * 9 : ���C�����X�g���[�g�t���b�V��
		 */
		
		
		for(int i=0;i<5;i++){
			aNumber[i] = p[0].getCardNumber(i);
			aSuit[i] = p[0].getCardSuit(i);
		}
		
		for(int i=0;i<5;i++){
			bNumber[i] = p[1].getCardNumber(i);
			bSuit[i] = p[1].getCardSuit(i);
		}
		
		//���[�U�[�̖𔻒�
		//�m�[�y�A�̔���
		if(aNumber[0] != aNumber[1] && aNumber[1] != aNumber[2] && aNumber[2] != aNumber[3] && aNumber[3] != aNumber[4]){
			aResult = 0;
		}
		
		//�t���b�V���̔���
		if(aSuit[0] == aSuit[1] && aSuit[0] == aSuit[2] && aSuit[0] == aSuit[3] && aSuit[0] == aSuit[4]){
			aResult = 5;
		}
		
		//�X�g���[�g�̔���
		if(aNumber[4]==aNumber[3]+1 && aNumber[3]==aNumber[2]+1 && aNumber[2]==aNumber[1]+1 && aNumber[1]==aNumber[0]+1){
			aResult = 4;
		}
		//�X�g���[�g�t���b�V���̔���
		else if(aNumber[4]==aNumber[3]+1 && aNumber[3]==aNumber[2]+1 && aNumber[2]==aNumber[1]+1 && aNumber[1]==aNumber[0]+1 && aNumber[1]!=aNumber[0]+9){
			aResult = 8;
		}
		//���C�����X�g���[�g�t���b�V���̔���
		else if(aNumber[0]==1 && aNumber[1]==10 && aNumber[2]==11 && aNumber[3]==12 && aNumber[4]==13 && aSuit[0]==aSuit[1] && aSuit[1]==aSuit[2] && aSuit[2]==aSuit[3] && aSuit[3]==aSuit[4]){
			aResult = 9;
		}
		
		//�t���n�E�X�̔���
		if(((aNumber[0]==aNumber[1]) && (aNumber[2]==aNumber[3] && aNumber[2]==aNumber[4])) ||
				((aNumber[0]==aNumber[1] && aNumber[0]==aNumber[2]) && (aNumber[3]==aNumber[4]))){
			aResult = 6;
		}
		
		//4�J�[�h�̔���
		if((aNumber[0]==aNumber[1] && aNumber[0]==aNumber[2] && aNumber[0]==aNumber[3]) ||
				(aNumber[1]==aNumber[2] && aNumber[1]==aNumber[3] && aNumber[1]==aNumber[4])){
			aResult = 7;
		}
		
		//3�J�[�h�̔���
		if(aResult != 7 && aResult != 6){
			for(int i=2;i<5;i++){
				if(aNumber[i-2]==aNumber[i-1] && aNumber[i-1]==aNumber[i]){
					aResult = 3;
				}
			}
		}
		
		//�P�y�A�A�Q�y�A�̔���
		if(aResult!=7 && aResult!=3){     //�R�J�[�h�ł��S�J�[�h�ł��Ȃ�������
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
		
		
		//CPU�̖𔻒�
		//�m�[�y�A�̔���
		if(bNumber[0] != bNumber[1] && bNumber[1] != bNumber[2] && bNumber[2] != bNumber[3] && bNumber[3] != bNumber[4]){
			bResult = 0;
		}
		
		//�t���b�V���̔���
		if(bSuit[0] == bSuit[1] && bSuit[0] == bSuit[2] && bSuit[0] == bSuit[3] && bSuit[0] == bSuit[4]){
			bResult = 5;
		}
		
		//�X�g���[�g�̔���
		if(bNumber[4]==bNumber[3]+1 && bNumber[3]==bNumber[2]+1 && bNumber[2]==bNumber[1]+1 && bNumber[1]==bNumber[0]+1){
			bResult = 4;
		}
		//�X�g���[�g�t���b�V���̔���
		else if(bNumber[4]==bNumber[3]+1 && bNumber[3]==bNumber[2]+1 && bNumber[2]==bNumber[1]+1 && bNumber[1]==bNumber[0]+1 && bNumber[1]!=bNumber[0]+9){
			bResult = 8;
		}
		//���C�����X�g���[�g�t���b�V���̔���
		else if(bNumber[0]==1 && bNumber[1]==10 && bNumber[2]==11 && bNumber[3]==12 && bNumber[4]==13 && bSuit[0]==bSuit[1] && bSuit[1]==bSuit[2] && bSuit[2]==bSuit[3] && bSuit[3]==bSuit[4]){
			bResult = 9;
		}
		
		//�t���n�E�X�̔���
		if(((bNumber[0]==bNumber[1]) && (bNumber[2]==bNumber[3] && bNumber[2]==bNumber[4])) ||
				((bNumber[0]==bNumber[1] && bNumber[0]==bNumber[2]) && (bNumber[3]==bNumber[4]))){
			bResult = 6;
		}
		
		//4�J�[�h�̔���
		if((bNumber[0]==bNumber[1] && bNumber[0]==bNumber[2] && bNumber[0]==bNumber[3]) ||
				(bNumber[1]==bNumber[2] && bNumber[1]==bNumber[3] && bNumber[1]==bNumber[4])){
			bResult = 7;
		}
		
		//3�J�[�h�̔���
		if(bResult != 7 && bResult != 6){
			for(int i=2;i<5;i++){
				if(bNumber[i-2]==bNumber[i-1] && bNumber[i-1]==bNumber[i]){
					bResult = 3;
				}
			}
		}
		
		//�P�y�A�A�Q�y�A�̔���
		if(bResult!=7 && bResult!=3){     //�R�J�[�h�ł��S�J�[�h�ł��Ȃ�������
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
		
				
	
	/** ��D�̖���\������ */
	public void print(){
		switch(aResult){
		case 0:
			System.out.println("���Ȃ��̎�D�́u�m�[�y�A�v�ł��B");
			break;
		case 1:
			System.out.println("���Ȃ��̎�D�́u�P�y�A�v�ł��B");
			break;
		case 2:
			System.out.println("���Ȃ��̎�D�́u�Q�y�A�v�ł��B");
			break;
		case 3:
			System.out.println("���Ȃ��̎�D�́u�R�J�[�h�v�ł��B");
			break;
		case 4:
			System.out.println("���Ȃ��̎�D�́u�X�g���[�g�v�ł��B");
			break;
		case 5:
			System.out.println("���Ȃ��̎�D�́u�t���b�V���v�ł��B");
			break;
		case 6:
			System.out.println("���Ȃ��̎�D�́u�t���n�E�X�v�ł��B");
			break;
		case 7:
			System.out.println("���Ȃ��̎�D�́u�S�J�[�h�v�ł��B");
			break;
		case 8:
			System.out.println("���Ȃ��̎�D�́u�X�g���[�g�t���b�V���v�ł��B");
			break;
		case 9:
			System.out.println("���Ȃ��̎�D�́u���C�����X�g���[�g�t���b�V���v�ł��B");
			break;
		}
		
		switch(bResult){       //CPU�̎�D�̖���\��
		case 0:
			System.out.println("CPU�̎�D�́u�m�[�y�A�v�ł��B");
			break;
		case 1:
			System.out.println("CPU�̎�D�́u�P�y�A�v�ł��B");
			break;
		case 2:
			System.out.println("CPU�̎�D�́u�Q�y�A�v�ł��B");
			break;
		case 3:
			System.out.println("CPU�̎�D�́u�R�J�[�h�v�ł��B");
			break;
		case 4:
			System.out.println("CPU�̎�D�́u�X�g���[�g�v�ł��B");
			break;
		case 5:
			System.out.println("CPU�̎�D�́u�t���b�V���v�ł��B");
			break;
		case 6:
			System.out.println("CPU�̎�D�́u�t���n�E�X�v�ł��B");
			break;
		case 7:
			System.out.println("CPU�̎�D�́u�S�J�[�h�v�ł��B");
			break;
		case 8:
			System.out.println("CPU�̎�D�́u�X�g���[�g�t���b�V���v�ł��B");
			break;
		case 9:
			System.out.println("CPU�̎�D�́u���C�����X�g���[�g�t���b�V���v�ł��B");
			break;
		}
	}
	
	
	
	
	/** ���ʂ�\������ */
	public void result(){
		if(aResult < bResult)    //���s��\��
			System.out.println("���Ȃ��̕����ł��B");
		else if(aResult > bResult)
			System.out.println("���Ȃ��̏����ł��B");
		else if(aResult == bResult)
			System.out.println("���������ł��B");
	}
	
}
