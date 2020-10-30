#include <bits/stdc++.h>
// 날짜 : 20201030  
// 작성자 : 김동우 
// 걸린 시간 : 06:41
using namespace std;

int main(void){
	int N,K;
	int answer=0;
	cin>>N>>K;
	int array[N];
	for (int i=0;i<N;++i){
		cin>>array[i];
	}
	for(int i=N-1;i>=0;--i){
		if(K>=array[i]){
			answer+=K/array[i];
			K-=(K/array[i])*array[i];
		}
	}
	cout<<answer;
	return 0;
}
