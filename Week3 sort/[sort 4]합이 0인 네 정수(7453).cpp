/*
# �ۼ��� : 20201113
# �ۼ��� : �赿��
# ������ : ���� 0�� �� ����
# ������� : �迭 4���� A,B,C,D�� �����ؼ� A[a] + B[b] + C[c] + D[d] == 0 �̵Ǵ� ������ ���ϱ�

# ���� �ؼ� :
# 1. ��� ������ ����Ѵٸ� ����� ���� �ʹ� �������� � ���Ҹ� ����ϵ� ���� 0�� �Ǵ� ���� ���� ã��

# ���� �� �� : solution 2���� �������� ������.
#16byte * 16,000,000 = 256,000,000 byte
# ���� ���� : �޸� �ʰ�
*/

#include <bits/stdc++.h>

using namespace std;

vector<long long> firstList;
vector<long long> secondList;
vector<long long> thirdList;
vector<long long> fourthList;


int main(){
    long long firstInput,secondInput,thirdInput,fourthInput;
    int N;
    cin>>N;
    // �Է¹ޱ� 
    for(int i=0;i<N;++i){
    	cin>>firstInput>>secondInput>>thirdInput>>fourthInput;
        firstList.push_back(firstInput);
        secondList.push_back(secondInput);
        thirdList.push_back(thirdInput);
        fourthList.push_back(fourthInput);
    }

	vector<long long> sumFirstSecondList;
	vector<long long> sumThirdFourthList; 
	// 0��° index�� 1��° index ���� ���� ���հ� 2��° index�� 3��° index ���� ���� ������ �����. 
	for(int firstIndex=0;firstIndex<firstList.size();firstIndex++){
		for(int secondIndex=0;secondIndex<secondList.size();secondIndex++){
			sumFirstSecondList.push_back(firstList[firstIndex]+secondList[secondIndex]);
			sumThirdFourthList.push_back(thirdList[firstIndex]+fourthList[secondIndex]);
		}
	}
	// ������������ �����Ѵ�. 
	sort(sumFirstSecondList.begin(),sumFirstSecondList.end());
	sort(sumThirdFourthList.begin(),sumThirdFourthList.end());

	int answer=0;
	int first=0;
    int end=sumThirdFourthList.size();
    int mid=(first+end)/2;
    int check=0;
    // 0��° index�� 1��° index������ ���հ�
    // 2��° index�� 3��° index�� ���� ������ ���� �� 0�� ��(answer)�� ã������
	// �̺�Ž�� ���� 

    for (int sumFirstSecondIndex=0;sumFirstSecondIndex<sumFirstSecondList.size();++sumFirstSecondIndex){	
        first=0;
        end=sumThirdFourthList.size()-1;
        mid=ceil((first+end)/2);
        check=0;
        // max��  13^13
        while(check<145){
            if (sumFirstSecondList[sumFirstSecondIndex]+sumThirdFourthList[mid]<0){
            	first=mid+1;
                mid=ceil((mid+end)/2);
			}
            else if(sumFirstSecondList[sumFirstSecondIndex]+sumThirdFourthList[mid]>0){
            	end=mid-1;
                mid=ceil((first+mid)/2);
			}
			else if(sumFirstSecondList[sumFirstSecondIndex]+sumThirdFourthList[mid]==0){
                answer+=1;
                break;
        	}
			check+=1;
		}
	}
	cout<<answer;
}
