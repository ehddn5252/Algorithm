#include <bits/stdc++.h>

using namespace std;
//savepoint 
bool check(int x, int y, int z);
int map1[9][9];
int ans=0;
int N;

void data_out(int answer){
	ofstream ofs;
	ofs.open("detroit.out");
	ofs<<answer;
	ofs.close();
	return ;
}

void detroit(){
	for(int i=0;i<N;i++){
		for(int j=0;j<N;++j){
			if(map1[i][j]==0){
				//밑에는 숫자를 확인하고 겹치는 것이 있다면 확인. 이부분이 핵심 
				for(int z=1;z<=N;++z){
					if(check(i,j,z)==1){
						map1[i][j]=z;
						detroit();
						map1[i][j] =0;
					}
				}
				//안채워진 디트로이트피자부분을 없애준다. 
				return ;
			}
		}
	}
	print()
	ans++;
	return ;
}

bool check(int x,int y, int z){
	//행 검사 그 행에 있는 것이 z랑 같은지 확인 
	for(int j=0;j<N;++j) {
		if(map1[x][j]==z){
			return false;
		}
	}
	// 열 검사 그 열에 있는 것이 z와 같은지 확인 
	for(int i=0;i<N;++i) {
		if(map1[i][y]==z){
			return false;
		}
	}
	return true;
}


int main(void){

	N=9
	for (int i=0;i<N;i++) {
		for(int j=0;j<N;++j){
			cin>>map1[i][j];
		}
	}
	detroit();

	//cout<<ans;
	data_out(ans);
	return 0;
}