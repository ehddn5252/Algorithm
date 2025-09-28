#include <iostream>
/*
*/
int main(){
    int n,m,tmp;
    int v[101]= {0,};
    for(int i=1;i<101;++i){
        v[i]=i;
    }
    std:: cin>> m>> n;
    for(int i =0;i<n;++i){
        int first,second;
        std:: cin>> first>> second;
        tmp = v[first];
        v[first] = v[second];
        v[second] = tmp;
    }
    for(int i=1;i<=m;++i){
        std:: cout<< v[i]<< " ";
    }
    return 0;
}