#include<iostream>
#include<vector>
using namespace std;

/*
*  
* 1. 상근이와 친구들은 오스트레일리아로 여행을 떠났다.
* 2. 상근이와 친구들은 총 M명이고, 지금 공항에서 한 줄로 서서 입국심사를 기다리고 있다.
* 3. 여러개의 입국 심사대가 있고 각 심사대마다 걸리는 시간이 다르다.
* 4. 이때, 모든 사람이 심사를 받는 데 걸리는 최소 시간을 구하여라.
*  첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ M ≤ 1,000,000,000)
한 심사대당 1,000,000,000 이 걸릴 수 있고, 인원이 1,000,000,000 이 걸릴 수 있기 때문에 최대 1,000,000,000 * 1,000,000,000 = 1,000,000,000,000,000,000 초가 걸릴 수 있다.
*/
#define MAX_VALUE 1000000000000000001;
// 1,000,000,000,000,000

int main() {
	cin.tie(0);
	cout.tie(0);
	// 입국 심사대의 수, 친구들 수
	int N, M;
	int tmp;
	unsigned long long ans = MAX_VALUE;
	cin >> N>> M;
	vector<int> v(N);
	unsigned long long minV = MAX_VALUE;

	// 입국 심사의 최소, 최댓값을 구한다.
	for (int i = 0; i < N; ++i) {
		cin >> tmp;
		v[i] = tmp;
		if (tmp < minV) {
			minV = tmp;
		}
	}

	unsigned long long left = minV, right = minV*M, mid=0;
	// 입국심사대마다 사용할 시간을 정해 놓는다. 
	// 그 시간만큼 입국심사대마다 사람을 통과시켜 통과시킨 사람의 수가 친구들 수와 같거나 크다면 그게 정답이 될 수 있다. 그리고 최적의 조건을 찾기위해 할당할 시간을 줄인다(right = mid-1);
	// 만약 통과시킨 인원이 작다면 입국심사대마다 할당할 시간을 더 많이 준다. (left = mid + 1;)
	while (left<=right) {
		mid = (left + right) / 2;
		unsigned long long peopleNum = 0;
		for (size_t i = 0; i < v.size(); ++i) {
			peopleNum+= mid/v[i];
		}
		if (peopleNum>=M) {
			ans = min(ans,mid);
			right = mid - 1;
		}
		else {
			left = mid + 1;
		}
	}

	cout << ans;

	return 0;
}