#include<iostream>
using namespace std;
#include<vector>

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int n,money,lastMoney;
	cin >> n;
	vector<int> coins = { 25,10,5,1 };
	const int COIN_TYPES = 4;
	for (int i = 0; i < n; ++i) {
		vector<int> ans = { 0,0,0,0 };
		cin >> money;
		lastMoney = money;

		for (int j = 0; j < COIN_TYPES; ++j) {
			ans[j] = (int)lastMoney / coins[j];
			lastMoney %= coins[j];
		}
		cout << ans[0] << " " << ans[1] << " " << ans[2] << " " << ans[3]<<endl;
	}
	return 0;
}