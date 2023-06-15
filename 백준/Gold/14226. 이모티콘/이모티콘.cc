#include<iostream>
#include<vector>

using namespace std;

/*
1. 이모티콘 s개를 보내려고 한다. s개의 이모티콘을 만드는 데 필요한 시간의 최솟값을 구하라.

1. 화면에 있는 모든 이모티콘을 복사해 클립보드에 저장
2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
3. 화면에 있는 이모티콘 중 하나를 삭제한다.

각 연산은 1초씩 걸린다.
현재 화면에는 이모티콘 하나가 저장되어 있는 상태이다.

s 개를 보낸다고 하면 s개에 가장 가까운 개수를 화면에 붙여놓고, 삭제하는 것

3개의 동작을 하는 과정을 계속해서 q에 넣고 반복하기

*/

#include<queue>

int main() {
	int n;
	const int MAX_VALUE = 2147483647;
	cin >> n;
	queue<vector<int>> q;
	q.push(vector<int>{0,1,0});
	
	vector<vector<int>> visit(2001, vector<int>(2001, MAX_VALUE));
	int maxAns = 10000;
	// {시간초, 화면에 있는 이모티콘 개수, 클립보드의 이모티콘 개수}
	while (!q.empty()) {
		vector<int> popped=q.front();
		q.pop();

		if (popped[1] >= n) {
			int tmpAns = popped[1] - n + popped[0];
			if (tmpAns < maxAns) {
				maxAns = tmpAns;
			}
			continue;
		}

		// 2가지 동작을 계속해서 반복하는 구문
		// 화면에 있는 이모티콘 클립보드에 덮어 쓰기
		if (visit[popped[1]][popped[1]] > popped[0] + 1) {
			visit[popped[1]][popped[1]] = popped[0] + 1;
			q.push({ popped[0] + 1,popped[1],popped[1] });
		}
		// 클립보드에 있는 모든 이모티콘 화면에 붙여넣기
		if (popped[1]+popped[2]<=2000 && visit[popped[1] + popped[2]][popped[2]] > popped[0] + 1) {
			visit[popped[1] + popped[2]][popped[2]] = popped[0] + 1;
			q.push({popped[0] + 1,popped[1] + popped[2],popped[2]});
		}
		if (popped[1] - 1 >= 0 && visit[popped[1] - 1][popped[2]] > popped[0] + 1) {
			visit[popped[1] - 1][popped[2]] = popped[0] + 1;
			q.push({ popped[0] + 1,popped[1] - 1 ,popped[2] });
		}
	}
	cout << maxAns;

	return 0;
}