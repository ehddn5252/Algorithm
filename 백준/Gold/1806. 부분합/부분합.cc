#include<iostream>
#include<vector>
using namespace std;



/* 아이디어
*
* 1. 왼쪽에서부터 부분합의 길이를 잰다.
* 2. 부분합의 합을 초과하면 앞에서부터 자른다.
* 3. 초과하지 않으면 뒤에서부터 더한다.

*/
#define ANS_MAX 2147483647
int main() {

	int N, S;

	cin >> N >> S;
	vector<long long> v(N);
	for (int i = 0; i < N; ++i) {
		cin >> v[i];
	}

	long long start = 0, end = 0, ans = ANS_MAX, nowLength = 0, nowNum = 0;
	while (end <= N && start < N) {
		if (nowNum >= S) {
			nowNum -= v[start++];
			if (ans > nowLength) {
				ans = nowLength;
			}
			nowLength -= 1;
		}
		else {
			if (end == N) {
				break;
			}
			nowNum += v[end++];
			nowLength += 1;
		}
	}
	if (ans == ANS_MAX) {
		ans = 0;
	}
	cout << ans;

	return 0;
}