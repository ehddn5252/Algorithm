#include<iostream>

using namespace std;
/* 나무 자르기 19:00 시작
* 
* 1. 절단기에 높이 H 를 지정한다.
* 2. 적어도 M 미터의 나무를 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력하라.


아이디어:

1. 이분 탐색으로 M 미터 값을 자른다고 표시해놓는다.
2. 이분 탐색으로 기준 값을 정해놓고 그 값을 기준으로 계속 길이를 높인다.

*/
#include<vector>
#include<algorithm>
int main() {

	// N 은 나무의 개수이고
	// M 은 최소 가져갈 나무 길이이다.
	long long N, M;
	cin >> N >> M;
	vector<int> v(N);
	long long end = 0;
	for (int i = 0; i < N; ++i) {
		cin >> v[i];
		if (v[i] > end) {
			end = v[i];
		}
	}
	
	sort(v.begin(), v.end());

	long long start = 0;

	long long mid = 0;
	long long ans = 0;
	while (start<=end) {
		mid = (start+end)/2;
		long long tmpHeight = 0;
		for (long long i = 0; i < N; ++i) {
			if (v[i] > mid) {
				tmpHeight += v[i]-mid;
			}
		}
		if (M <= tmpHeight) {
			start = mid + 1;
			ans = mid;
		}
		else{
			end = mid - 1;
		}
	}
	cout << ans <<endl;

	return 0;
}