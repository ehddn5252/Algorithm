#include<iostream>
#include<set>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int iCount=0, jCount=0;
    int sSize = s.size();
    for (int i = 0; i < sSize; ++i) {
        if (s[i] == 'I' || s[i] == 'J') {
            if (i + 2 < sSize && s[i + 1] == 'O' && s[i + 2] == 'I') {
                if (s[i] == 'I') {
                    iCount += 1;
                }
                else{
                    jCount += 1;
                }
            }
        }
    }
    cout << jCount << endl<<iCount;
    return 0;
}