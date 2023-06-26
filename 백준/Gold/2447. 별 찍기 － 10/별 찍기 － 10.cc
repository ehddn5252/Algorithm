#include<iostream>
#include<vector>

using namespace std;

/*
1. 재귀적인 패턴으로 별을 찍어야 한다. N이 3의 거듭제곱이라 할 때, 가운데에 공백이 있고 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.


어떻게 할까?

아이디어
가운데를 빼고 다 칠하게 하는 로직을 만든다.
예를 들어 n= 27, x = 27/ 3이라고 하면 x+1  ~ 2x 까지는 비워야 한다. 그러고 재귀로 들어가는 로직 사용하기

*/

vector<vector<char>> v;
void recur(int inputI, int inputJ, int n) {
	if (n == 1) return;

	int x = n / 3;
	for (int i = inputI; i < inputI+ n; ++i) {
		for (int j = inputJ; j < inputJ+ n; ++j) {
			if (j >= inputJ+x && j < inputJ+ 2 * x && i>= x +inputI && i < 2 * x+inputI) {
				v[i][j] = ' ';
			}
		}
	}
	
	recur(inputI, inputJ, n / 3);
	recur(inputI+n/3, inputJ, n / 3);
	recur(inputI, inputJ+n/3, n / 3);
	recur(inputI + 2* n / 3, inputJ, n / 3);
	recur(inputI, inputJ + 2 * n / 3, n / 3);
	recur(inputI + n/3, inputJ + 2 * n / 3, n / 3);
	recur(inputI + 2 * n / 3, inputJ + n/3, n / 3);
	recur(inputI + 2 * n / 3, inputJ + 2 * n / 3, n / 3);
}




int main() {

	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		vector<char> tmpV(n);
		for (int j = 0; j < n; ++j) {
			tmpV[j] = '*';
		}
		v.push_back(tmpV);
	}
	recur(0, 0, n);
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cout << v[i][j];
		}
		cout << endl;
	}
	return 0;
}