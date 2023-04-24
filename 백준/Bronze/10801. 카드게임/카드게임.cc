#include<iostream>


using namespace std;


int main() {

	int aCount = 0, bCount = 0;
	int GAME_ROUND = 10;
	int aNum[10];
	int bNum[10];
	
	
	
	int tmp;
	for (int i = 0; i < GAME_ROUND; ++i) {
		cin >> tmp;
		aNum[i] = tmp;
	}
	for (int i = 0; i < GAME_ROUND; ++i) {
		cin >> tmp;
		bNum[i] = tmp;
	}
	for (int i = 0; i < GAME_ROUND; ++i) {
		if (aNum[i] > bNum[i]) {
			aCount += 1;
		}
		else if (aNum[i] < bNum[i]) {
			bCount += 1;
		}
	}

	if (aCount > bCount) {
		cout << "A";
	}
	else if (aCount < bCount) {
		cout << "B";
	}
	else {
		cout << "D";
	}
	
	return 0;
}