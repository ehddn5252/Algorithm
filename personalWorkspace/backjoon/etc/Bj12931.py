# 두 배 더하기
'''
1. 모든 값이 0으로 채워져 있는 길이가 N인 배열A가 있따. 영선이는 다음과 같은 두 연산을 수행할 수 있다.
- 배열에 있는 값 하나를 1 증가시킨다.
- 배열에 있는 모든 값을 두 배 시킨다.

배열 B가 주어졌을 때, 배열 A를 B로 만들기 위한 연산의 최소 횟술르 구하는 프로그램을 작성하시오.

- DFS로 모든 경우의 수를 확인한다.
1. 숫자 하나를 1 올리는 것,
2. 숫자 전체를 2배하는 것
?? 이게 되나

- DP에 저장해야 한다.
- 반대로 빼면서 한다.

전체를 2로 나눌 수 있으면 2로 나눈다.
그게 아니면 1을 뺀다.

'''

import sys
num=int(sys.stdin.readline())
num_l: list = list(map(int, sys.stdin.readline().split(" ")))

def can_divid(num):
    return

ans=0
while(True):
    divid_flag=True
    check_ans=True
    for v in num_l:
        if(v!=0):
            check_ans=False

    if(check_ans):
        print(ans)
        break

    for i,v in enumerate(num_l):
        if v%2!=0:
            divid_flag=False
            num_l[i]-=1
            ans+=1

    check_ans=True
    for v in num_l:
        if(v!=0):
            check_ans=False

    if(check_ans):
        print(ans)
        break

    for i,v in enumerate(num_l):
        num_l[i]/=2
    ans+=1

