#include<iostream>
#include<vector>
#include<queue>
using namespace std;
/*
1. 빙하가 녹고있다.
2. 빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장된다. 빙산 이외의 바다에 해당하는 칸에는 0이 저장된다. 그림 1에서 빈칸은 모두 0으로 채워져 있다고 생각한다.
바닷물에 많이 접해있는 부분이 더 빨리 줄어든다. 한 덩이의 빙산이 주어질 때 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간을 구하는 프로그램을 작성하시오.

아이디어

BFS로 주변에 바다에 접한 면만큼 녹는 로직 사용하고, 매 초마다 확인하는 check문을 사용한다.


*/
int dI[4] = {-1,1,0,0};
int dJ[4] = { 0,0,-1,1 };

vector<vector<int>> v;
queue<pair<int, int>> q;
vector<vector<bool>> visit;
void dfs(int inputI, int inputJ) {
	for (int i = 0; i < 4; ++i) {
		int nextI = dI[i] + inputI;
		int nextJ = dJ[i] + inputJ;
		if (nextI < 0 || nextI >= v.size() || nextJ < 0 || nextJ >= v[0].size()) continue;
		if (!visit[nextI][nextJ] && v[nextI][nextJ] != 0) {
			visit[nextI][nextJ] = true;
			dfs(nextI, nextJ);
		}
	}
}



int main() {


	int N, M;

	cin >> N >> M;
	vector<int> vTmp(M);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			cin >> vTmp[j];
			if (vTmp[j] != 0) {
				q.push(make_pair(i, j));
			}
		}
		v.push_back(vTmp);
	}
	vector<vector<int>> nextV(v);
	int time = 0;
	while(true){
		int qSize = q.size();
		// v.assign(nextV.size(), vector<int>(nextV.size()));
		
		for (int qIndex = 0; qIndex< qSize;++qIndex){
			pair<int, int> popped = q.front();
			q.pop();
			int minusPoint = 0;
			for (int i = 0; i < 4; ++i) {
				int nextI = dI[i] + popped.first;
				int nextJ = dJ[i] + popped.second;
				if (nextI < 0 || nextI >= N || nextJ < 0 || nextJ >= M) continue;
				if (v[nextI][nextJ] == 0) {
					minusPoint += 1;
				}
			}
			if (minusPoint >= v[popped.first][popped.second]) {
				nextV[popped.first][popped.second] = 0;
			}
			else {
				q.push(make_pair(popped.first, popped.second));
				nextV[popped.first][popped.second] -= minusPoint;
			}
		}
		copy(nextV.begin(), nextV.end(), v.begin());
		time += 1;
		// 여기에서 빙산이 갈라졌는 지 dfs로 확인.
		bool isSplited = false;
		bool breakFlag = false;
		bool allMelt = true;
		visit.assign(N,vector<bool>(M,false));
		for(int i=0;i<N;++i){
			for (int j = 0; j < M; ++j) {
				if (v[i][j] != 0) {
					allMelt = false;
				}
				if(!visit[i][j] && v[i][j]!=0) {
					if (isSplited) {
						breakFlag = true;
						break;
					}
					isSplited = true;
					dfs(i, j); 
				}
			}
			if (breakFlag) {
				break;
			}
		}
		if (breakFlag) {
			break;
		}
		if (allMelt) {
			time = 0;
			break;
		}
	}
	cout << time;
	return 0;
}
