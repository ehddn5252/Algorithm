#include<iostream>
#include<cmath>
#include<string>
using namespace std;

#define MAXIMUM 1003002

bool isNotPrimes[MAXIMUM] = { false, };


void primeChecker() {
	for (int i = 2; i < MAXIMUM; ++i) {
		int jRange = (int)sqrt(i) + 1;
		for (int j = 2; j < jRange; ++j) {
			if (i % j == 0) {
				isNotPrimes[i] = true;
				break;
			}
		}
	}
}

bool checkPelindrum(int num) {
	string s;
	s = to_string(num);
	int sSize = (int) s.size() / 2 + 1;
	for (int i = 0; i < sSize; ++i) {
		if (s[i] != s[s.size() - 1 - i]) {
			return false;
		}
	}
	return true;
}

int checkAnswer(int n) {
	n = (n >1) ? n : 2;
	for (int i = n; i < MAXIMUM; ++i) {
		if (!isNotPrimes[i]) {
			if (checkPelindrum(i)) {
				return i;
			}
		}
	}
}

// n 보다 크거나 같은 소수이면서 펠린드림 수 중 가장 작은 값을 구하여라.
int main() {
	primeChecker();

	int n;
	cin >> n;
	cout<< checkAnswer(n)<<endl;

	return 0;
}