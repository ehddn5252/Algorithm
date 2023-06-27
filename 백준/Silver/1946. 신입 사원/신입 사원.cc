#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

/*
1. 신규 사원 채용 1차 2찰 이루어짐
2. 다른 모든 지원자와 비교했을 때 A 지원자의 성적이 B의 지원자 성적보다 1차 2차 모두 떨어진다면 안 뽑는다.
3. 2번 위 조건을 만족하는 선발가능 신입사원의 최대 인원수를 구하여라.

아이디어
1. 1차 면접은 내림차순 2차 면접은 1차가 같을 시 오름 차순으로 정렬
2. 1차 점수가 높은 사원의 2차면접 점수를 다른 사원들과 비교를 한다.
3. 1차도 낮고 2차도 낮은 사원이 있다면 제거
4. 제거하고 남은 인원 수가 답


*/

bool compare(pair<int,int> a, pair<int, int> b) {
	if (a.first != b.first) {
		return a.first < b.first;
	}
	else {
		return a.second > b.second;
	}
}


int main() {
	int testcase;
	cin >> testcase;

	for (int testcaseIndex = 0; testcaseIndex < testcase; ++testcaseIndex) {
		int n;
		cin >> n;
		vector<pair<int, int>> v(n);
		vector<bool> visit(n);
		fill(visit.begin(), visit.end(), false);
		
		int tmpA, tmpB;
		for (int i = 0; i < n; ++i) {
			cin >> tmpA >> tmpB;
			v[i]=make_pair(tmpA, tmpB);
		}
		
		sort(v.begin(), v.end(), compare);
		
		int start = 0;
		int compare = 1;
		visit[start] = true;
		while(compare<v.size()){
			if (v[start].second > v[compare].second) {
				visit[compare] = true;
				start = compare;
			}
			compare += 1;
		}
		int ans = 0;
		for (int i = 0; i < n; ++i) {
			ans += visit[i];
		}
		cout << ans<<endl;
	}
	return 0;
}