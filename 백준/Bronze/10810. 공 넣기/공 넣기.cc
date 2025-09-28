#include <iostream>
/*
N개의 바구니
번호가 적혀있는 M번 공을 넣음.
공을 넣을 바구니 범위에 넣음.
이미 바구니에 공이 있는 경우 빼고 새로 공을 넣음

입력: 
N M
start_basket end_basket ball_number

해결 방법: 
1. 처음 바구니 n개 세팅.
2. start end ball_number로 넣을 때마다 해당 바구니ball number로 업데이트
*/
int main(){
    int n,m;

    std:: cin>> n>>m;
    int basket[101]={0,};
    for(int i=0;i<m;i++){
        int start,end,ball;
        std::cin>>start>>end>>ball;
        for(int j=start;j<=end;j++){
            basket[j]=ball;
        }
    }
    for(int i=1;i<=n;i++){
        std::cout<<basket[i]<<" ";
    }
    return 0;
}