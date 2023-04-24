#include<iostream>


int main() {
	int n;
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);
	std::cin >> n;
	std::string str;
	for (int i = 0; i < n; ++i) {
		std::cin >> str;

		for (int j = 0; j < str.length(); ++j) {
			if (str[j]<=90) {
				std::cout << (char)(str[j] + 32);
			}
			else {
				std::cout << str[j];
			}
		}
		std::cout << std::endl;
	}

	return 0;
}