#include<iostream>

using namespace std;


int main() {
	int a_score = 0, a, b, c, d;
	int b_score = 0;

	cin >> a >> b >> c >> d;
	a_score += a;
	a_score += b;
	a_score += c;
	a_score += d;
	cin >> a >> b >> c >> d;

	b_score += a;
	b_score += b;
	b_score += c;
	b_score += d;

	if (a_score >= b_score) {
		cout << a_score;
	}
	else {
		cout << b_score;
	}
	return 0;
}