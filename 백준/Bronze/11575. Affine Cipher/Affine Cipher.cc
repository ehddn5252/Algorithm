#include<iostream>
#include<string>

using namespace std;

int main() {
	int testcase,A,B;
	string s;

	cin >> testcase;

	for (int i = 0; i < testcase;++i) {
		cin >> A >> B;
		cin >> s;
		for (int i = 0; i < s.length(); ++i) {
			cout << (char)(((s[i] - 65) * A + B) % 26+65);
		}
		cout << endl;

	}
	return 0;
}