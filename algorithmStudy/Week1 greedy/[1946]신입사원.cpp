#include <bits/stdc++.h>
// ������ ����� �ڵ�
using namespace std;

bool compare(pair<int,int> a,pair<int,int> b){
	return a.first<b.first;
}

int main(void){
	int T,N,tmp1,tmp2,bound=0,answer=0;
	vector<int> answerList;
	cin>>T;
	for(int i=0;i<T;++i){
		cin>>N;
		answer=N;
		pair<int,int> p1[N];
		for(int j=0;j<N;++j){
			cin>>tmp1>>tmp2;
			p1[j]=make_pair(tmp1,tmp2);
		}
		sort(&p1[0],&p1[N],compare);
		bound=p1[0].second;
		for(int j=1;j<N;++j){
			if(p1[j].second>bound) answer--;
			bound=min(bound,p1[j].second);
			
		}
		answerList.push_back(answer);
	}
	for(int i=0;i<T;++i){
		cout<<answerList[i]<<endl;
	}

	return 0;
}
