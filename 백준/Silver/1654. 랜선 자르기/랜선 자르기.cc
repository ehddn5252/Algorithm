#include<iostream>
#include<vector>

using namespace std;
/* 랜선 자르기

1. K개의 랜선으로 N 개의 랜선을 만들어야 한다.
2. 이때 만들 수 있는 랜선 길이의 최대 길이를 구하라
*/



int main() {

	cin.tie(0);
	cout.tie(0);
	int n, k, tmp;
	long long end = 0;
	vector<int>v;
	cin >> n>>k;
	for (size_t i = 0; i < n; ++i) {
		cin >> tmp;
		v.push_back(tmp);
		if (tmp > end) {
			end = tmp;
		}
	}

	long long start = 1;
	long long mid=0;
	int ans=1;
	while (start <= end) {
		mid = (start + end) / 2;
		long long lanNum=0;
		for (size_t i = 0; i < n; ++i) {
			lanNum+=v[i] / mid;
		}
		if (lanNum >= k) {
			ans = mid;
			start = mid + 1;
		}
		else {
			end = mid - 1;
		}
	}

	cout << ans;
	return 0;
}