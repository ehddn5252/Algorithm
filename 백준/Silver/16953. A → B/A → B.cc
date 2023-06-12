#include<iostream>
#include<array>
#include<queue>
using namespace std;


/*
1. 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

- 2를 곱한다.
- 1을 수의 가장 오른쪽에 추가한다.
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

1,000,000,000
10억 개이다.

2,147,483,647


*/

queue<pair<long long int,int>> q;

int main() {
	int times = 0;
	long long int a;
	int b;
	bool can_make = false;
	cin >> a >> b;
	pair<long long int, int> p = make_pair(a, 1);
	q.push(p);
	while (!q.empty()) {
		pair<long long int,int> popped = q.front();
		q.pop();
		if (popped.first<b){
			if (popped.first < 1000000001) {
				q.push(make_pair<long long int, int>(popped.first*2, popped.second + 1));
				q.push(make_pair<long long int, int>(popped.first*10+1, popped.second + 1));
			}
		}
		else if(popped.first ==b){
			cout << popped.second;
			can_make = true;
			break;
		}
	}
	if (!can_make) {
		cout << -1;
	}
	return 0;
}