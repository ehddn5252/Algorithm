#include <bits/stdc++.h>
// 날짜 : 20201102 10:30 
// 작성자 : 김동우 
// 걸린 시간 : 01:30:00 포기. 
// 1차 고비 : 문제를 반대로 읽어서 내림차순으로 정렬했음 
// 2차 고비 : 왜 안되누?  시간초과인가?
// 원인 생각 : 이전 코드와 비교를 해봤다. 다른 점은 여기에서는 구조체를 사용해서
//			    미리 메모리를 할당한 반면 이전 코드에서는 그때그때 pair를 사용하여
//				그때그떄  메모리를 추가했다.

using namespace std;

//#define testprint


typedef struct stru1{
	int test1;
	int test2;
}stru1;

bool cmp(const stru1 &a,const stru1 &b){
	return a.test1<b.test1;
}

stru1 a[20][100000];

int main(void){
	int T;
	cin>>T;
	int N[T]={0,};
	int pibot=0;	
	vector<int> answer;
	for(int i=0;i<T;++i){
		cin>>N[i];
		answer.push_back(N[i]);
		for(int j=0;j<N[i];++j){
			cin>>a[i][j].test1>>a[i][j].test2;
		}
		sort(a[i],a[i]+N[i],cmp);
		
		for(int j=1;j<N[i];++j){
			if(a[i][pibot].test2<a[i][j].test2){
				answer[i]--;
			}
			else{
				pibot=j;
			}	
		}
		
	}
	#ifdef testprint
	cout<<"for testprint start=================="<<endl;
	for(int i=0;i<T;++i){
		cout<<"Testcase "<<i+1<<endl;
		for(int j=0;j<N[i];++j){
			cout<<a[i][j].test1<<" "<<a[i][j].test2<<endl;
		}
	}
	cout<<"for testprint end===================="<<endl;
	#endif
	
	for(int i=0;i<T;++i){
		cout<<answer[i]<<endl;
	}
	return 0;
}
