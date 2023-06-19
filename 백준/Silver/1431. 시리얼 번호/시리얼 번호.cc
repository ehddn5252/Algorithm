#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

bool compare(pair<int, string> a, pair<int, string> b) {
    if (a.second.size() != b.second.size()) {
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

int getSumOfDigits(string s) {
    int sum = 0;
    for (char c : s) {
        if (isdigit(c)) {
            sum += c - '0';
        }
    }
    return sum;
}

int main() {
    int n;
    cin >> n;

    vector<pair<int, string>> v(n);
    for (int i = 0; i < n; ++i) {
        cin >> v[i].second;
        v[i].first = getSumOfDigits(v[i].second);
    }

    sort(v.begin(), v.end(), compare);

    for (auto& p : v) {
        cout << p.second << '\n';
    }

    return 0;
}
