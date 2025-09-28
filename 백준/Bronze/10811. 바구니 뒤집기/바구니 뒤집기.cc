#include <iostream>
/*
5 4
1 2
3 4
1 4
2 2

*/
int main(){
    int n,m,tmp;
    int v[101];
    for(int i=1;i<=100;++i){
        v[i] = i;
    }
    std::cin >> n >> m;
    for(int i=0;i<m;++i){
        int first,second;
        std::cin >> first >> second;
        for(int j=first;j<=(second+first)/2;++j){
            tmp = v[j];
            v[j] = v[second-j+first];
            v[second-j+first] = tmp;
        }
    }
    for(int i=1;i<=n;++i){
        std::cout<< v[i]<< " ";
    }
    return 0;
}