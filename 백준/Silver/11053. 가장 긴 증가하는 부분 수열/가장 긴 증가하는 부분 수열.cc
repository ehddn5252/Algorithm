
#include<iostream>
#include<vector>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> v(n);
	vector<int> dp(n);

	fill(dp.begin(), dp.end(), 1);
	for (int i = 0; i < n; ++i) cin >> v[i];

	unsigned long long maxValue = 1;
	for (int i = 0; i < n; ++i) {
		for (int j = i+1; j < n; ++j) {
			if (v[j] > v[i]) {
				dp[j] = max(dp[i] + 1, dp[j]);
				dp[j] > maxValue ? maxValue = dp[j] : maxValue;
			}
		}
	}

	cout << maxValue;
	/*
	1. 가장 긴 증가하는 수열 2 문제인데, 일단은 가장 긴 증가하는 수열을 하는 방법부터 만들어야 한다.
	
	// 가장 긴 증가하는 수열 만드는 방법 1 dp. 아래 방법을 사용하면 풀린다.
	vector<int> v(n);
	vector<int> dp(n);

	fill(dp.begin(), dp.end(), 1);
	for (int i = 0; i < n; ++i) cin >> v[i];


	for (int i = 0; i < n; ++i) {
		for (int j = i+1; j < n; ++j) {
			if (v[j] > v[i]) {
				dp[j] = max(dp[i] + 1, dp[j]);
			}
		}
	}
	for (auto& a : dp) {
		cout << a << endl;
	}

	이제 이거를 시간을 줄여야 한다. 
	n이 1,000,000 이라서 n^1.5 를 하면 1,000,000,000 10억은 돈다.
	어떻게 해야 줄일 수 있을까? 힌트는 이분탐색이라던데,
	이분 탐색이라면 이분탐색으로 찾을 target 을 정해야 한다. 

	target 으로는 증가하는 수열의 개수? 이걸 하려면 이미 다 저장되어 있어야 하므로 pass

	인덱스 정보? 
	*/

	return 0;
}