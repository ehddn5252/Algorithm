/*
# 작성일 : 20201113
# 작성자 : 김동우
# 문제명 : 합이 0인 네 정수
# 문제요약 : 배열 4개를 A,B,C,D를 선택해서 A[a] + B[b] + C[c] + D[d] == 0 이되는 순서쌍 구하기

# 문제 해설 :
# 1. 모든 조합을 사용한다면 경우의 수가 너무 많아질듯 어떤 원소를 사용하든 합이 0이 되는 것의 수를 찾기

# 질문 본 후 : solution 2개의 집합으로 나눈다.
#16byte * 16,000,000 = 256,000,000 byte
# 실패 요인 : 메모리 초과
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
    // 입력받기 
    for(int i=0;i<N;++i){
    	cin>>firstInput>>secondInput>>thirdInput>>fourthInput;
        firstList.push_back(firstInput);
        secondList.push_back(secondInput);
        thirdList.push_back(thirdInput);
        fourthList.push_back(fourthInput);
    }       
    
	vector<long long> sumFirstSecondList;
	vector<long long> sumThirdFourthList; 
	// 0번째 index와 1번째 index 값을 더한 집합과 2번째 index와 3번째 index 값을 더한 집합을 만든다. 
	for(int firstIndex=0;firstIndex<firstList.size();firstIndex++){
		for(int secondIndex=0;secondIndex<secondList.size();secondIndex++){
			sumFirstSecondList.push_back(firstList[firstIndex]+secondList[secondIndex]);
			sumThirdFourthList.push_back(thirdList[firstIndex]+fourthList[secondIndex]);
		}
	}
	// 오름차순으로 정렬한다. 
	sort(sumFirstSecondList.begin(),sumFirstSecondList.end());
	sort(sumThirdFourthList.begin(),sumThirdFourthList.end());
	
	int answer=0;
	int first=0;
    int end=sizeof(sumThirdFourthList)/sizeof(long long)-1;
    int mid=(first+end)/2;
    int check=0;
    // 0번째 index와 1번째 index를더한 집합과
    // 2번째 index와 3번째 index를 더한 집합을 더한 게 0인 값(answer)을 찾기위한
	// 이분탐색 구현 
	for (int sumFirstSecondIndex=0;sumFirstSecondIndex<sumFirstSecondList.size();++sumFirstSecondIndex){	
        first=0;
        end=sumThirdFourthList.size()-1;
        mid=ceil((first+end)/2);
        check=0;
        // max가  13^13
        while(check<145){
            if (sumFirstSecondList[sumFirstSecondIndex]+sumThirdFourthList[mid]<0){
            	first=mid;
                mid=ceil((mid+end)/2);
			}
            else if(sumFirstSecondList[sumFirstSecondIndex]+sumThirdFourthList[mid]>0){
            	end=mid;
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

