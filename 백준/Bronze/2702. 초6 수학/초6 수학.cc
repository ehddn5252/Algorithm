#include<iostream>

using namespace std;


int findLCM(int a,int b, int gcd) {
	return a * b / gcd;
}
int findGCD(int a, int b) {
	int ret;
	int max_value = max(a, b);
	int min_value = min(a, b);
	for (int i = max_value; i >=1 ; --i) {
		if (a % i == 0 && b % i == 0) {
			return i;
		}
	}
}


int main()
{
	int LCM, GCD;

	int n;

	cin >> n;
	int a, b;
	for (int i = 0; i < n; ++i) {
		cin >> a >> b;
		GCD = findGCD(a, b);
		LCM = findLCM(a, b, GCD);
		cout << LCM << " " << GCD << endl;
	}
	return 0;
}