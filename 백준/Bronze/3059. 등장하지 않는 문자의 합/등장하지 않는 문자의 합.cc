#include<iostream>

using namespace std;

int main() {
	int testcase;
	int ALPHABET_NUM = 26;
	string str;

	cin >> testcase;
	
	for (int i = 0; i < testcase; ++i) {
		bool  b[26] = { false ,};
		int ans = 0;
		cin >> str;
		for (int j = 0; j < str.length(); ++j) {
			b[str[j] - 65] = true;
		}
		for (int j = 0; j < ALPHABET_NUM; ++j) {
			if (!b[j]) {
				ans += j + 65;
			}
		}
		cout << ans << endl;
	}
	return 0;
}