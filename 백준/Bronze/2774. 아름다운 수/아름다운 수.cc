#include<iostream>
#include<set>
using namespace std;

int main()
{
    int n;
    string tmp;
    cin >> n;
    for (auto i = 0; i < n; ++i) {
        set<int> nums;
        cin >> tmp;
        
        for (int j = 0; j < tmp.size(); ++j) {
            nums.insert((int)tmp[j]);
        }
        cout << nums.size() << endl;
    }

    return 0;
}