
#include<iostream>
#include<vector>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> v(n);
	vector<int> lis;
	
	for (int i = 0; i < n; ++i) cin >> v[i];
	lis.push_back(v[0]);

	int length = 1;
	for (int i = 1; i < v.size(); ++i) {
		if (v[i] > lis.back()) {
			length += 1;
			lis.push_back(v[i]);
		}
		else {
			int left = 0;
			int right = length;
			int mid;
			while (left < right) {
				mid = (left + right)/2;
				if (lis[mid]< v[i]) {
					left = mid + 1;
				}
				else {
					right = mid;
				}
			}
			lis[left] = v[i];
		}
	}
	cout << length;

	return 0;
}