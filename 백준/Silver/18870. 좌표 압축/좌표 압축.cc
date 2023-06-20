#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;
#include<set>
/*
1. 수직선 위에 N개의 좌표 X1, X2 ... Xn이 있다. 
2. Xi 를 압축한 결과 X`i 값은 Xi>Xj 를 만족하는 서로 다른 좌표 Xj의 개수와 같아야한다.
3. 압축을 적용한 결과를 출력하라.
-10^9 <= Xn <= 10^9
1,000,000,000
*/

/* 생각

좌표 압축을 해야 하는데, pq에 넣어서 log(1,000,000) = 1,000 * 1,000,000 = 1,000,000,000



*/

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	size_t n;
	cin >> n;
	set<int> s;
	map<int, int> map1;
	vector<int> v(n);
	int tmp;
	for (size_t i = 0; i < n; ++i) {
		cin >> tmp;
		v[i]=tmp;
		s.insert(tmp);
	}
	vector<int> v2(s.begin(), s.end());
	sort(v2.begin(), v2.end());
	int index = 0;
	for (auto i = v2.begin(); i != v2.end(); ++i) {
		map1[*i] = index;
		index += 1;
	}
	for (int i = 0; i < n; ++i) {
		printf("%d ",map1[v[i]]);
	}
	return 0;
}