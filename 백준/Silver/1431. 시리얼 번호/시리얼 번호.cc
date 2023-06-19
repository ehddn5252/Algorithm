#include<iostream>
#include<algorithm>
/*
1. 시리얼 번호 A가 시리얼 번호 B의 앞에 오는 경우는 다음과 같다.

- 길이가 다르면 짧은 것이 먼저 온다.
- 길이가 같다면 A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저 온다.
- 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
*/
#include<vector>
#include<string>
using namespace std;

bool compare(pair<int,string> a,pair<int,string> b) {
	if (a.second.size() != b.second.size()){
		return a.second.size() < b.second.size();
	}
	else {
		if (a.first != b.first) {
			return a.first < b.first;
		}
		else {
			return a.second < b.second;
		}
	}
}



int main() {

	vector<pair<int,string>> v;

	int n;
	string tmp;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> tmp;
		string news;
		int sumV = 0;
		for(int j=0;j<tmp.size();++j){
			if ('9' >= tmp[j] && tmp[j] >= '0') {
				sumV += tmp[j]-'0';
			}
		}
		v.push_back(make_pair(sumV, tmp));
	}
	sort(v.begin(),v.end(),compare);
	for (auto i = 0; i < v.size(); ++i) {
		cout << v[i].second << endl;
	}

	return 0;
}