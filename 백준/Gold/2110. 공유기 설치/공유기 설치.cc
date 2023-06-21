#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

/*
1. k개의 공유기를 N개의 집에 설치한다.
2. 가장 인접한 두 공유기 사이 거리가 최대가 되게 설치하고 그 거리를 출력하시오
*/


int main() {

	int n,k,tmp;
	long long ans = 0;
	// n개의 집 k개의 공유기
	cin >> n >> k;
	
	vector<int> v(n);
	long long end=0,mid=0;
	for (size_t i = 0; i < n; ++i) {
		cin >> tmp;
		v[i] = tmp;
	}
	sort(v.begin(),v.end());
	long long start = 1;
	end = v[n-1];
	while (start <= end) {
		mid = (start + end) / 2;
		int kNum = 1;
		long long before = v[0];
		for (size_t i = 1; i < n; ++i) {
			if (v[i] - before>=mid) {
				kNum += 1;
				before = v[i];
			}
		}
		// 설치한 것이 설치해야 하는 것보다 적으면
		if(kNum<k){
			end = mid -1;
		}
		// 설치한 것이 설치해야 하는 것보다 많으면
		else if(kNum>=k){
			ans = max(mid, ans);
			start = mid+1;
		}
	}
	cout << ans;
	return 0;
}