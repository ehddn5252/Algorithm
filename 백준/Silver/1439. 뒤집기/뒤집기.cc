#include<iostream>


using namespace std;
/*
아이디어

0을 뒤집어야 하는 경우와 1을 뒤집어야 하는 경우 2 가지를 확인합니다.

*/


int main() {
	string s;
	cin >> s;
	int oneAns = 0;
	// 모두 1로 만들어야 하는 경우
	for (int i = 0; i < s.size(); ++i) {
		if (s[i] == '0') {
			oneAns += 1;
			for (int j = i+1; j < s.size(); ++j) {
				if (s[j] == '1') {
					break;
				}
				else {
					i += 1;
				}
			}
		}
	}
	int zeroAns = 0;
	// 모두 0 으로 만들어야 하는 경우
	for (int i = 0; i < s.size(); ++i) {
		if (s[i] == '1') {
			zeroAns += 1;
			for (int j = i + 1; j < s.size(); ++j) {
				if (s[j] == '0') {
					break;
				}
				else {
					i += 1;
				}
			}
		}
	}
	cout << min(oneAns,zeroAns);

	return 0;
}