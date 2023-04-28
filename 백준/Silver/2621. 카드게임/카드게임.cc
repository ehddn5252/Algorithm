#include<iostream>
#include<algorithm>
using namespace std;
/* 카드 게임 - 카드의 점수를 계산하여 출력하라.
* 점수를 정하는 규칙
* 1. 카드 5장이 모두 같은 색이면서 숫자가 연속적일 때, 가장 높은 숫자에 900을 더한다.
* 2. 5장 중 4장의 숫자가 같을 때 같은 색 숫자에 800 더한다.
* 3. 3장이 같고 2장이 같으면 3장의 숫자에 10을 곱하고 2장의 숫자를 더한다음 700을 더한다. 
* 4. 5장의 카드 색깔이 모두 같으면 가장 높은 숫자에 600을 더한다.
* 5. 5장 숫자가 연속되면 가장 높은 숫자에 500을 더한다.
* 6. 3장의 숫자가 같으면 같은 숫자에 400을 더한다.
* 7. 5장 중 2장의 숫자가 같고 다른 2장의 숫자가 같을 때 점수는 같은 숫자 중 큰 숫자에 10을 고하고 같은 숫자 중 작은 숫자를 더한 다음 300을 더한다.
* 8. 5장 중 2장의 숫자가 같을 때 점수는 같은 숫자에 200을 더한다.
* 9. 아무 경우도 아니면 가장 큰 숫자에 100을 더한다.
*/

#define CARD_MAXIMUM 5

enum CARD_RANK{
	STRAIGHT_FLUSH=900, FOUR_CARD=800, FULL_HOUSE=700, FLUSH=600, STRAIGHT=500, THRIPLE=400, TWO_PAIR=300, ONE_PAIR=200, HIGH_CARD=100
};


bool isFlush(char* color){
	// check color
	char first = color[0];
	for (int i = 1; i < CARD_MAXIMUM; ++i) {
		if (color[i] != color[0]) {
			return false;
		}
	}
	return true;
}

bool isStraight(int* num) {
	int start = num[0];
	for (int i = 1; i < CARD_MAXIMUM; ++i) {
		if (num[i] - start != 1) {
			return false;
		}
		start = num[i];
	}
	return true;
}

pair<CARD_RANK,int> getSameCardRank(int* num) {
	CARD_RANK ret = CARD_RANK::HIGH_CARD;
	int cardNum = 0;
	int sameCardQuantity[2] = { 1,1 };
	int sameCardNum[2] = { 0,0 };

	int num1 = num[0];
	int sameCardIndex = 0;
	for (int i = 1; i < CARD_MAXIMUM; ++i) {
		if (num[i] == num1) {
			sameCardQuantity[sameCardIndex] += 1;
			sameCardNum[sameCardIndex] = num[i];
		}
		else {
			num1 = num[i];
			if (sameCardQuantity[sameCardIndex]>1) {
				sameCardIndex += 1;
			}
			if (sameCardIndex>=2) {
				break;
			}
		}
	} // CARD CHECK;
	int before = max(sameCardQuantity[0], sameCardQuantity[1]);
	for (int i = 0; i < 2; ++i) { // 여기에서 
		if (sameCardQuantity[i] == 4) {
			ret = CARD_RANK::FOUR_CARD;
			cardNum = sameCardNum[i];
			return make_pair(ret, cardNum);
		}
		else if (sameCardQuantity[i] ==3) {
			if (sameCardQuantity[1 - i] == 2) {
				ret = CARD_RANK::FULL_HOUSE;
				cardNum = sameCardNum[i] * 10 + sameCardNum[1 - i];
			}
			else {
				ret = CARD_RANK::THRIPLE;
				cardNum = sameCardNum[i];
			}
			return make_pair(ret, cardNum);
		}

		else if (before<= sameCardQuantity[i] && sameCardQuantity[i] ==2) {
			if (sameCardQuantity[1 - i] == 2) {
				ret = CARD_RANK::TWO_PAIR;
				cardNum = max(sameCardNum[i],sameCardNum[1-i])*10 + min(sameCardNum[i], sameCardNum[1-i]);
			}
			else {
				ret = CARD_RANK::ONE_PAIR;
				cardNum = sameCardNum[i];
			}
			return make_pair(ret, cardNum);
		}
	} // get rank
	return make_pair(ret, cardNum);
}
#define f(x) #x
int main() {
	int ret = 0, num[CARD_MAXIMUM];
	char color[CARD_MAXIMUM];

	for (int i = 0; i < CARD_MAXIMUM; ++i) {
		cin >> color[i] >> num[i];
	}
	sort(num, num + CARD_MAXIMUM);
	const int MIN_VALUE = num[0];
	const int MAX_VALUE = num[4];

	bool straight, flush;
	pair <CARD_RANK, int> sameCardret;
	sameCardret = getSameCardRank(num);
	straight = isStraight(num);
	flush = isFlush(color);
	
	if (straight && flush) {
		ret = CARD_RANK::STRAIGHT_FLUSH + MAX_VALUE;
	}
	else if (sameCardret.first == CARD_RANK::FOUR_CARD) {
		ret = sameCardret.second + CARD_RANK::FOUR_CARD;
	}
	else if (sameCardret.first == CARD_RANK::FULL_HOUSE) {
		ret = sameCardret.second + CARD_RANK::FULL_HOUSE;
	}
	else if (flush) {
		ret = CARD_RANK::FLUSH+ MAX_VALUE;
	}
	else if (straight) {
		ret = CARD_RANK::STRAIGHT + MAX_VALUE;
	}
	else if (sameCardret.first == CARD_RANK::THRIPLE) {
		ret = sameCardret.second + CARD_RANK::THRIPLE;
	}
	else if (sameCardret.first == CARD_RANK::TWO_PAIR) {
		ret = sameCardret.second + CARD_RANK::TWO_PAIR;
	}
	else if (sameCardret.first == CARD_RANK::ONE_PAIR) {
		ret = sameCardret.second + CARD_RANK::ONE_PAIR;
	}
	else if (sameCardret.first == CARD_RANK::HIGH_CARD) {
		ret = MAX_VALUE + CARD_RANK::HIGH_CARD;
	}
	cout << ret;
	return 0;
}