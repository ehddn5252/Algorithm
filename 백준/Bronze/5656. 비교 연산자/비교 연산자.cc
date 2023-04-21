#include<iostream>
using namespace std;


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int a, b,caseNum=1;
	string oper;
	
	while (true) {
		bool isTrue = false;
		cin >> a >> oper >> b;

		if (oper == "E") {
			break;
		}
		else if (oper == ">") {
			if (a > b) {
				isTrue = true;
			}
		}
		else if (oper == ">=") {
			if (a >= b) {
				isTrue = true;
			}
		}
		else if (oper == "<") {
			if (a < b) {
				isTrue = true;
			}
		}
		else if (oper == "<=") {
			if (a <= b) {
				isTrue = true;
			}
		}
		else if (oper == "==") {
			if (a == b) {
				isTrue = true;
			}
		}
		else if (oper == "!=") {
			if (a != b) {
				isTrue = true;
			}
		}
		if (isTrue) {
			cout << "Case " << caseNum << ": true" << endl;
		}
		else {
			cout << "Case " << caseNum << ": false" << endl;
		}
		caseNum += 1;
	}
	
	
	
	return 0;
}