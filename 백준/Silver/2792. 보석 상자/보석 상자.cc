#include<iostream>

using namespace std;
/*
1. 각각의 보석은 M 가지 서로 다른 색상 중 한 색상이다.
2. 학생은 같은 색상의 보석만 가져간다.
3. 질투심이 최소가 되게 나누어주는 방법을 알아내시오.
4. 질투심은 가장 많은 보석을 가져간 학생이 가지고 있는 보석의 개수이다.



아이디어

일단 한 사람당 한 가지 색상만 받을 수 있다. 
그리고 보석들의 종류가 여러 개라서 이를 사람당으로 나눠야한다.

아이들의 수는 최대 1,000,000,000 이고 색상의 수는 30만이다.
아이들의 수가 색상의 수보다 항상 많다.

1. 이분 탐색으로 해야할 듯
2. 일단 최대 가져가는 보석의 개수를 m개로 한다.
*/
#include<vector>
int main() {
	int N, M;
	cin >> N >> M;
	vector<long long> v(M);
	int end = 0;
	for (int i = 0; i < M; ++i) {
		cin >> v[i];
		if (v[i] > end) {
			end = v[i];
		}
	}
	int start = 0;
	int mid = 0;
	int ans = 0;
	while (start <= end) {
		mid = (start + end) / 2;
		if (mid == 0) {
			ans = end;
			break;
		}
		int mMax = N;
		for(int i = 0; i < v.size(); ++i){
			// 보석의 개수 나누기 최대 줄 수 있는 것의 수는   
			if(v[i]%mid==0){
				mMax -= v[i] / mid;
			}
			else {
				mMax -= v[i] / mid +1;
			}
		}
		if (mMax<0) {
			start = mid + 1;
		}
		else {
			ans = mid;
			end = mid - 1;
		}
	}
	cout << ans << endl;
	return 0;
}