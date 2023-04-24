#include<iostream>


using namespace std;

int main() {

	int testcase;

	cin >> testcase;
	int n;
	char player1, player2;
	for (int i = 0; i < testcase; ++i) {
		cin >> n;
		int player1Score = 0;
		int player2Score = 0;
		for(int j=0;j<n;++j){
			cin >> player1 >> player2;
			if (player1 != player2) {
				if (player1 == 'R') {
					if (player2 == 'S') {
						player1Score += 1;
					}
					else if (player2 == 'P') {
						player2Score += 1;
					}
				}
				if (player1 == 'S') {
					if (player2 == 'P') {
						player1Score += 1;
					}
					else if (player2 == 'R') {
						player2Score += 1;
					}
				}
				if (player1 == 'P') {
					if (player2 == 'R') {
						player1Score += 1;
					}
					else if (player2 == 'S') {
						player2Score += 1;
					}
				}
			}
		}
		if (player1Score > player2Score) {
			cout << "Player 1"<<endl;
		}
		else if (player1Score < player2Score) {
			cout << "Player 2" << endl;
		}
		else {
			cout << "TIE" << endl;
		}
	}
	return 0;
}