#include<iostream>
#include<vector>
#include<string>
#include<cmath>
using namespace std;

void hanoi(int start, int end, int via, int times) {
	if (times == 1) {
		printf("%d %d\n", start, end);
	}
	else{
		hanoi(start, via, end, times - 1);
		printf("%d %d\n", start, end);
		hanoi(via, end, start, times - 1);
	}
}

int main() {

	int N;
	cin >> N;
	string ans = to_string(pow(2, N));
	
	int x = ans.find('.');
	ans = ans.substr(0, x);
	ans[ans.length() - 1] -= 1;
	
	cout << ans<<endl;
	if (N <= 20) {
		hanoi(1, 3, 2, N);
	}
	
	return 0;
}