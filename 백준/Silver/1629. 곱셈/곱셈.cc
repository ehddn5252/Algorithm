#include<iostream>

using namespace std;

/* 곱셈
A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
A,B,C는 각각 2147483647보다 적은 숫자이다. 이를 C로 나눈 나머지를 어찌 구할꼬~

-> A ^ B % C 구하기

(a + b) % M = (a % M + b % M) % M 을 이용해서 푼다.
*/
long long ans = 1;
long long divid(long long a, long long b, long long c) {
	if (b == 1) {
		return a%c;
	}
	long long tmp = divid(a, b / 2, c);
	
	if (b % 2 == 0) {
		return tmp * tmp % c;
	}
	else {
		return tmp * tmp % c * a % c;
	}
	
}

int main() {
	long long a, b, c;
	cin >> a >> b >> c;

	cout << divid(a, b, c);
	return 0;
}