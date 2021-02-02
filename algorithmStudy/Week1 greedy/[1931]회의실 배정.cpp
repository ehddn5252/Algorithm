#include <bits/stdc++.h>

//#define TESTPRINT

using namespace std;

bool cmp(pair<int,int> p1,pair<int,int> p2){
	if(p1.second<p2.second){
		return true;
	}
	else if(p1.second==p2.second){
		return p1.first<=p2.first;
	}
	else {
		return false;
	}
}

int main(void){
	int N;
	int pivot=0,answer=1;
	cin>>N;
	pair<int,int> p[N];

	for(int i=0;i<N;++i){
		cin>>p[i].first>>p[i].second;
	}
	sort(&p[0],&p[N],cmp);
	for(int i=1;i<N;++i){
		if(p[pivot].second<=p[i].first){
			answer++;
			pivot=i;
		}
	}
	#ifdef TESTPRINT
	cout<<"for testprint start=================="<<endl;
	for(int i=0;i<N;++i){
		cout<<p[i].first<<" "<<p[i].second<<endl;
	}
	cout<<"for testprint end===================="<<endl;
	#endif

	cout<<answer<<endl;
	return 0;
}