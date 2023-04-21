#include<iostream>
using namespace std;
#include<vector>
#include<algorithm>

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string cases = "CAMBRIDGE";
	string ans_str = "";
	string input_str;
	cin >>input_str;
	for (int i = 0; i < input_str.size(); ++i) {
		bool isNotIn = true;
		for (int j = 0; j < cases.length(); ++j) {
			if (cases[j] == input_str[i]) {
				isNotIn = false;
				break;
			}
		}
		if (isNotIn) {
			ans_str += input_str[i];
		}
	}
	cout << ans_str;
	return 0;
}