#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<cmath>
using namespace std;

/*
송도에 사는 상근이와 친구들 
락패까지 가야한다.
락페에서 송도까지 갈 때, 편의점 마다 거리가 1km 이하여야 끝까지 갈 수 있다.
끝까지 갈 수 있는 지 확인하시오

아이디어
1. vector<bool> visit(n), 시작점에서부터 다음 위치의 거리가 1km 이하면 넣고 방문 표시를 한다.
2. 락페까지 갔으면 hapy 아니면 sad 출력
*/

bool isCanGo(int x, int y, int nextX, int nextY) {

	int ret = abs(x - nextX) + abs(y - nextY);
	if (ret <= 1000) {
		return true;
	}
	else {
		return false;
	}
}

int main() {
	int testcase;

	cin >> testcase;
	for (int testcaseIndex = 0; testcaseIndex < testcase; ++testcaseIndex) {
		int n;
		cin >> n;

		vector<bool> visit(n+2);
		fill(visit.begin(), visit.end(), false);
		visit[0] = true;

		queue<pair<int, int>> q;

		vector<pair<int, int>> v(n+2);
		for (int i = 0; i < n+2; ++i) {
			int tmpX, tmpY;
			cin >> tmpX >> tmpY;
			v[i]=make_pair(tmpX, tmpY);
			if (i == 0) {
				q.push(make_pair(tmpX, tmpY));
			}
		}
		bool breakFlag = false;
		while (!q.empty()) {
			pair<int, int> p = q.front();
			q.pop();
			for (int i = 0; i < n + 2; ++i) {
				if (!visit[i]) {
					if(isCanGo(p.first,p.second,v[i].first,v[i].second)){
						if(i == n + 1) {
							cout << "happy" << endl;
							breakFlag = true;
							break;
						}
						visit[i] = true;
						q.push(v[i]);
					}
				}
			}
			if (breakFlag) {
				break;
			}
		}

		if(!breakFlag){
			cout << "sad" << endl;
		}
	}
	return 0;
}