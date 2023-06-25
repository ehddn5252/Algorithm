#include<iostream>
#include<vector>

using namespace std;

/*
문제
잘라진 하얀색 색종이의 개수와 파란색 색종이의 개수를 차례로 출력하라.
1이 파란색 0이 하얀색이다.

아이디어
재귀로 4등분한다.

*/
enum Color {
	white = 0, blue = 1
};

int whiteNum = 0;
int blueNum = 0;
vector<vector<int>> v;

void recur(int startI, int startJ, int max, int colorFlag) {
	if (max == 1) {
		if (colorFlag == Color::white) {
			if (v[startI][startJ] == Color::white) {
				whiteNum += 1;
			}
		}
		else {
			if (v[startI][startJ] == Color::blue){
				blueNum += 1;
			}
		}
		return;
	}
	bool break_flag = false;
	for (int i = startI; i < startI + max; ++i) {
		for (int j = startJ; j < startJ + max;++j) {
			if (v[i][j] != colorFlag) {
				recur(startI, startJ, max / 2, colorFlag);
				recur(startI + max / 2, startJ, max / 2, colorFlag);
				recur(startI, startJ + max / 2, max / 2, colorFlag);
				recur(startI + max / 2, startJ + max / 2, max / 2, colorFlag);
				break_flag = true;
				break;
			}
		}
		if (break_flag) {
			break;
		}
	}
	if (!break_flag) {
		if (colorFlag == Color::white) {
			whiteNum += 1;
		}
		else {
			blueNum += 1;
		}
	}
	return ;
}

int main() {
	int N;

	cin >> N;
	// vector<vector<int>> v(N);
	for (int i = 0; i < N; ++i) {
		vector<int> tmpV(N);
		for(int j = 0; j < N; ++j) {
			cin >> tmpV[j];
		}
		v.push_back(tmpV);
	}
	recur(0, 0, N, Color::blue);
	recur(0, 0, N, Color::white);

	cout << whiteNum << endl << blueNum;
	return 0;
}