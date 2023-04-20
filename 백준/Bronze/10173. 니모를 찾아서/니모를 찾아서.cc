#include<iostream>

#include<string>

using namespace std;

int main() {
	string s;
	while (true) {
		getline(cin, s);
		if (s == "EOI") {
			break;
		}
		bool isFound = false;
		for (int i = 0; i < s.length(); ++i) {
			if (tolower(s[i]) == 'n' && i + 3 < s.length() && tolower(s[i + 1]) == 'e' && tolower(s[i + 2]) == 'm' && tolower(s[i + 3]) == 'o') {
				cout << "Found" << endl;
				isFound = true;
				break;
			}
		}
		if (!isFound) {
			cout << "Missing" << endl;
		}
	}
	return 0;
}