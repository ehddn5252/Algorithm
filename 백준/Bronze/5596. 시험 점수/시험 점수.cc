#include<iostream>

using namespace std;


int main() {
	int a_score = 0, b_score = 0, num;
	for (int i = 0; i < 4; ++i) {
		cin >> num;
		a_score += num;
	}
	
	for (int i = 0; i < 4; ++i) {
		cin >> num;
		b_score += num;
	}

	if (a_score >= b_score) {
		cout << a_score;
	}
	else {
		cout << b_score;
	}
	return 0;
}