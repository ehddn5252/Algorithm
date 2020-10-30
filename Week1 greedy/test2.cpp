#include <bits/stdc++.h>
// 날짜 : 20201030  
// 작성자 : 김동우 
// 걸린 시간 : 30:00
using namespace std;

int main(void){
	vector<int> L,P,V,answer;
	int a,b,c=2;
	for (;;){
		cin>>a>>b>>c;
		if (a==0&&b==0&&c==0){
			break;
		}
		L.push_back(a);
		P.push_back(b);
		V.push_back(c);
		answer.push_back(0);
	}
	for (int i=0;i<L.size();++i){
		answer[i]+=(V[i]/P[i])*L[i];
		if(L[i]>V[i]%P[i]){
			answer[i]+=V[i]%P[i];
		}
		else{
			answer[i]+=L[i];
		}
	}
	
	for(int i=0;i<answer.size();++i){
		cout<<"Case "<<(i+1)<<": "<<answer[i]<<endl;
	}
		
	return 0;
}
