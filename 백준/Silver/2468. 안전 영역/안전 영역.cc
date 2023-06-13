#include<iostream>

/* 안전 영역
* 1. 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사하려고 한다. 



*/

/* 방법
* 비의 양을 1로 설정한다.
* 지역을 처음부터 끝까지 한번 쭉 돌아본다.
* 안전영역을 체크하면서 visit한다.
* 다 돌았으면 안전영역 개수를 global에 최신화한다.
* 비의 양을 1 늘리고 위를 반복한다.
*/

#include<vector>
#include<queue>

using namespace std;
vector<vector<short>> v;
vector<vector<bool>> visit;
short globalTimes= 1;
int di[4] = {0,0,-1,1};
int dj[4] = { -1,1,0,0 };
int n;

void bfs(int inputI,int inputJ,int high) {
	queue<pair<int,int>> q;
	visit[inputI][inputJ] = true;
	pair<int, int> initPair = make_pair(inputI, inputJ);
	q.push(initPair);
	while (!q.empty()){
		pair<int, int> popped = q.front();
		q.pop();
		// visit[popped.first][popped.second] = true;
		for (int i = 0; i < 4; ++i) {
			int nextI = popped.first + di[i];
			int nextJ = popped.second + dj[i];
			if (nextI >= n or nextI < 0 or nextJ >= n or nextJ < 0) continue;
			if (visit[nextI][nextJ])continue;
			if (high >= v[nextI][nextJ]) {
				continue;
			}
			visit[nextI][nextJ] = true;
			pair<int, int> tmpPair= make_pair(nextI,nextJ);
			q.push(tmpPair);
		}
	}
}

int main() {

	int maxValue = 0;
	int ans = 0;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		vector<short> tmpS;
		vector<bool> tmpB;
		for (int j = 0; j < n; ++j) {
			short tmpNum;
			cin >> tmpNum;

			if (maxValue < tmpNum) {
				maxValue = tmpNum;
			}

			tmpS.push_back(tmpNum);
			tmpB.push_back(false);
		}
		v.push_back(tmpS);
		visit.push_back(tmpB);
	}
	
	for(int high=0; high <maxValue;++high){
		// visit 초기화
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				visit[i][j] = false;
			}
		}
		int rigionNum= 0;

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (!visit[i][j] && high <v[i][j]) {
					bfs(i, j,high);
					rigionNum  += 1;
				}
			}
		}
		if (rigionNum > ans) {
			ans = rigionNum;
		}
	}
	cout << ans;
	return 0;
}
