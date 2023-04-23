#include<iostream>
#include<string>
#include<fstream>
using namespace std;


int main() {

	string N;
	getline(cin, N);
	int n = stoi(N);
	for (int i = 1; i <= n; ++i) {
		string str;
		getline(cin, str);
		cout << i << ". " << str << endl;
	}
	return 0;
}