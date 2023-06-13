#include<iostream>
#include<vector>
/*
* 외판원 순회
* 1. 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다.
* 2. 가장 적은 비용으로 N개의 도시를 거치는 여행 루트를 짤 때, 비용을 출력하시오
*/
/* Solution. BFS
* 1. DFS 로 모든 경로를 탐색한다.
* 2. 하나의 비용이 정해지면 그 비용보다 큰 경우는 가지치기를 한다.
* 
*/

using namespace std;

vector<vector<int>> v;
vector<bool> visit;
int n;
int globalCost = 2147483647;

void dfs(int start,int nowCost, int nodeNum) {

	// 다 방문했으면 globalCost보다 적은지 확인한다.
	int s = 0;
	for (int i = 0; i < visit.size(); ++i) {
		s += visit[i];
	}
	if (nowCost > globalCost) {
		return ;
	}
	if (s == n) {
		if (nowCost < globalCost) {
			globalCost= nowCost;
		}
		return ;
	}
	for (int i = 0; i < n; ++i) {
		if (s != n - 1 && i == start) continue;
		if (i == nodeNum || v[nodeNum][i]==0)continue;
		if (!visit[i]) {
			visit[i] = true;
			dfs(start,nowCost + v[nodeNum][i], i);
			visit[i] = false;
		}
	}
}


int main() {
	cin >> n;
	for (int i = 0; i < n; ++i) {
		vector<int > tmpV;
		int tmp;
		for (int j = 0; j < n; ++j) {
			cin >> tmp;
			tmpV.push_back(tmp);
		}
		v.push_back(tmpV);
		visit.push_back(false);
	}
	
	for (int i = 0; i < n; ++i) {
		dfs(i,0, i);
	}
	cout << globalCost;

	return 0;
}