#include<iostream>
using namespace std;
#include<vector>
#include<algorithm>


template<typename a>
int calc(a T) {
	int ret=0;
	sort(T.begin(), T.end());
	if (T[0] == T[1] && T[1] == T[2] && T[2] == T[3]) {
		ret += T[0] * 5000+50000;
	}
	else if (T[0] == T[1] && T[1] == T[2]) {
		ret += 10000 + T[1] * 1000;
	}
	else if (T[1] == T[2] && T[2] == T[3]) {
		ret += 10000 + T[1] * 1000;
	}
	else if (T[0] == T[1] && T[2] == T[3]) {
		ret += 2000 + T[0] * 500 + T[2] * 500;
	}
	else if (T[0] == T[1] || T[1] == T[2] ||T[2] == T[3]) {
		if (T[0] == T[1]) {
			ret += 1000 + 100 * T[0];
		}
		else if (T[1] == T[2]) {
			ret += 1000 + 100 * T[1];
		}
		else if (T[2] == T[3]) {
			ret += 1000 + 100 * T[2];
		}
			
	}
	else {
		ret +=T[3]*100;
	}
	

	return ret;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int n;
	cin >> n;
	/* case는 5개
	* 1. 4개 같다.
	* 2. 3개 같다.
	* 3. 2개 2쌍이 같다.
	* 4. 2개 같다.
	* 5. 1개 같다.
	*/

	int a,ans=0;
	int money;
	for (int i = 0; i < n; ++i) {
		vector<int> nums;
		for (int j = 0; j < 4; ++j) {
			cin >> a;
			nums.push_back(a);
			
		}
		money = calc(nums);
		if (money > ans) {
			ans = money;
		}
	}
	cout << ans << endl;;
	return 0;
}