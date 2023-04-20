#include<iostream>
#include<string>

using namespace std;
int main() {
	string s;
	cin >> s;
	for (int i = 0; i < s.length(); ++i) {
		cout << char((s[i] - 65 - 3 + 26) % 26 + 65);
	}
	return 0;
}