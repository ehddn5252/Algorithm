#include<iostream>
#include<vector>
#include<queue>
#include<list>
#include<algorithm>
using namespace std;

/*
1 이면 익은 토마토 0은 익지 않은 토마토 -1 은 토마토가 없음
-> bfs 사용

*/


int di[4] = {0,0,-1,1};
int dj[4] = {-1,1,0,0};
int main() {

	int m,n;
	cin >> m>>n;
	int tmp;
	vector<vector<int>> v;
	vector<vector<bool>>visit;
	queue<vector<int>> q;
	for (int i = 0; i < n; ++i) {
		vector<bool> tmpV;
		for (int j = 0; j < m; ++j) {
			tmpV.push_back(false);
		}
		visit.push_back(tmpV);
	}
	for (int i = 0; i < n; ++i) {
		vector<int> tmpV;
		for (int j = 0; j < m; ++j) {
			cin >> tmp;
			tmpV.push_back(tmp);
			if (tmp == 1) {
				visit[i][j] = true;
				q.push({ 0,i, j });
			}
		}
		v.push_back(tmpV);
	}
	int maxTime = 0;

	while (!q.empty()) {
		vector<int> front =q.front();
		int time = front[0];
		int posI = front[1];
		int posJ = front[2];
		q.pop();
		for (int i = 0; i < 4; ++i) {
			int nextI = posI + di[i];
			int nextJ = posJ + dj[i];

			if (nextI >= n or nextI < 0 or nextJ >= m or nextJ < 0) continue;
			if (visit[nextI][nextJ] != 0) continue;
			if (visit[nextI][nextJ]) continue;
			if (v[nextI][nextJ] == 0) {
				visit[nextI][nextJ] = true;
				q.push({ time + 1,nextI, nextJ });
				maxTime = maxTime > time + 1 ? maxTime: time + 1;
			}
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (v[i][j] == 0 && visit[i][j] == false) {
				maxTime = -1;
				cout << maxTime;
				return 0;
			}
		}
	}
	cout << maxTime;

	return 0;
}