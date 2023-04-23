#include<iostream>


using namespace std;


int main() {


	int N,aWin=0,bWin=0,a,b;

	cin >> N;
	for (int i = 0; i < N; ++i) {
		cin >> a >> b;
		if (a > b) {
			aWin += 1;
		}
		else if (a < b) {
			bWin += 1;
		}
	}
	cout << aWin << " " << bWin;
	return 0;

}