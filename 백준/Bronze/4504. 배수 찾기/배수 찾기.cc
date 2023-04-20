#include<iostream>


using namespace std;


int main() {
	int n, num;
	cin >> n;
	while (true) {
		cin >> num;
		if (num == 0) {
			break;
		}
		if (num < n) {
			cout << num << " is NOT a multiple of " << n << "." << endl;
		}
		else {
			if (num % n == 0) {
				cout << num << " is a multiple of " << n << "." << endl;
			}
			else {
				cout << num << " is NOT a multiple of " << n << "." << endl;
			}
		}
	}
	return 0;
}