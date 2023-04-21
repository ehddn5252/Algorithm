#include<iostream>
using namespace std;
#include<vector>

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	const short MAX_LENGTH = 8;
	string s;
	for (int i = 0; i < 3; ++i) {
		cin >> s;
		int max_value = 1;
		char before = s[0];
		int now_count = 1;
		for (int i = 1; i < MAX_LENGTH; ++i) {
			if (before == s[i]) {
				now_count+=1;
				if (max_value < now_count) {
					max_value = now_count;
				}
			}
			else {
				now_count = 1;
				before = s[i];
			}
		}
		cout << max_value<<endl;
	}
	return 0;
}