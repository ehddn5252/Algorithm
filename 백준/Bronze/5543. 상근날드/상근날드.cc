#include <iostream>

using namespace std;


int main(){
    int minBurger = 2147483647;
    int minCoke = 2147483647;
    int num;
    for(int i=0;i<3;++i){
        cin>>num;
        if (num <minBurger){
            minBurger = num;
        }
    }
    for(int i=0;i<2;++i){
        cin>>num;
        if (num<minCoke){
            minCoke = num;
        }
    }
    int result = minBurger+minCoke-50;
    cout << result;
    return 0;
}