#include<iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n,tmp;
	int v[10001] = { 0, };
	cin >> n;

	for (int i = 0; i < n; ++i) {
		cin >> tmp;
		v[tmp] +=1;
	}
	
	for (int i = 1; i < 10001; ++i) {
		while(v[i]--){
			printf("%d\n", i);
		}
	}
	return 0;
}