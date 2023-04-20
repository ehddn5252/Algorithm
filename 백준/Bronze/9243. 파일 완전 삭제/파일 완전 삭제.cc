#include<iostream>


using namespace std;


int main() {


	int n;
	string bitA,bitB;
	cin >> n;
	cin >> bitA;
	cin>>bitB;
	string ans = "Deletion succeeded";
	if (n % 2 == 0) {
		if (bitA != bitB) {
			ans = "Deletion failed";
		}
	}
	else{
		for (int i = 0;i<bitA.size();++i) {
			if (bitA[i] == bitB[i]) {
				ans = "Deletion failed";
				break;
			}
		}
	}
	cout << ans;

	return 0;
}