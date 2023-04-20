#include<iostream>
#include<string>
#include<sstream>
using namespace std;


int main() {


	int n;
	string s;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		int start = 26 * 26;
		cin >> s;
		int first = 1;
		for (int j = 0; j < 3; ++j) {
			first += int(s[j]-65) * start;
			start /= 26;
		}
		int tmp;
		stringstream ssInt(s.substr(4, 8));
		ssInt >> tmp;
		first -= tmp;
		if (abs(first) <= 100) {
			cout << "nice" << endl;
		}
		else {
			cout << "not nice" << endl;
		}
	}
	return 0;
}