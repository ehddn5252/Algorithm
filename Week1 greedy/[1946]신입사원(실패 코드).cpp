#include <bits/stdc++.h>
// ��¥ : 20201102 10:30 
// �ۼ��� : �赿�� 
// �ɸ� �ð� : 01:30:00 ����. 
// 1�� ��� : ������ �ݴ�� �о ������������ �������� 
// 2�� ��� : �� �ȵǴ�?  �ð��ʰ��ΰ�?
// ���� ���� : ���� �ڵ�� �񱳸� �غô�. �ٸ� ���� ���⿡���� ����ü�� ����ؼ�
//			    �̸� �޸𸮸� �Ҵ��� �ݸ� ���� �ڵ忡���� �׶��׶� pair�� ����Ͽ�
//				�׶��׋�  �޸𸮸� �߰��ߴ�.

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
