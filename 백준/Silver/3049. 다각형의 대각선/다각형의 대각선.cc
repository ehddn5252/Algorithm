#include<iostream>

using namespace std;


int main() {

	int n;
	cin >> n;
	
	int ans = 1;
	for (int i = n; i >= 0 && i >= n - 3; --i) {
		ans *= i;
		ans /= n - i+1;
	}
	cout << ans;
	return 0;
}