#include<iostream>
#include<set>
using namespace std;

int main()
{
    int n,tmp;
    cin >> n;
    set<int> nums;
    for (auto i = 0; i < n; ++i) {
        
        cin >> tmp;
        nums.insert(tmp);
        
    }
    cout << n- nums.size() << endl;

    return 0;
}