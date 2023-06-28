#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;


int main() {

	vector<pair<int, int>> v;
	priority_queue<int, vector<int>, greater<int>>pqGreater;
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		int startTime, endTime;
		cin >> startTime >> endTime;
		v.push_back(make_pair(startTime, endTime));
	}

	sort(v.begin(), v.end());
	pqGreater.push(v[0].second);

	for (int i = 1; i < v.size(); ++i) {
		pqGreater.push(v[i].second);

		if (pqGreater.top() <= v[i].first) {
			pqGreater.pop();
		}
	}
	cout << pqGreater.size();
	return 0;
}