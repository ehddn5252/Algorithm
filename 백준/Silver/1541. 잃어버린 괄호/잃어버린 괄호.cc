#include<iostream>
#include<string>
using namespace std;

// +와 -로 이루어진 식이 주어지고, 이 식에 괄호를 칠 수 있다. 괄호를 쳐서 가장 작은 수로 만들 방법을 구하시오.
// 앞에 마이너스가 있는 경우 그 다음에는 모든 값을 마이너스로 만들 수 있다.
int main() {

	string s;
	cin >> s;
	int ans = 0;
	string numS = "";
	int num = 0;
	bool minusFlag = false;
	for (int i = 0; i < s.size(); ++i) {
		if (s[i] != '-' && s[i] != '+') {
			numS += s[i];
		}
		else {
			num = stoi(numS);
			if (minusFlag) {
				ans -= num;
			}
			else {
				ans += num;
			}
			if (s[i] == '-') {
				minusFlag = true;
			}
			numS = "";
		}
	}
	num = stoi(numS);
	if (minusFlag) {
		ans -= num;
	}
	else {
		ans += num;
	}
	cout << ans;
	return 0;
}