#include<iostream>

using namespace std;


int main() {
	int m, day;
	cin >> m>> day;

	if (31 + 18 > (m - 1) * 31 + day) {
		cout << "Before";
	}
	else if (31 + 18 < (m - 1) * 31 + day) {
		cout << "After";
	}
	else {
		cout << "Special";
	}
	return 0;
}