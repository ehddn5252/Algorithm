#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<set>
using namespace std;


int main() {
	int n;
	vector<string> v;
	string s;
	set<string> stringSet;

	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> s;
		stringSet.insert(s);
	}

	for (auto i = stringSet.begin(); i != stringSet.end(); ++i) {
		v.push_back(*i);
	}
	vector<bool> visit(v.size());
	fill(visit.begin(), visit.end(), true);

	sort(v.begin(), v.end());

	const size_t vSize = v.size();
	for (int i = 0; i < vSize; ++i) {
		for (int j = i + 1; j < vSize; ++j) {
			if (v[j].substr(0, min(v[j].size(), v[i].size())).compare(v[i]) == 0) {
				visit[i] = false;
				break;
			}
		}
	}
	int ans = 0;
	for (int i = 0; i < visit.size(); ++i) {
		ans += visit[i];
	}

	cout << ans;

	return 0;
}