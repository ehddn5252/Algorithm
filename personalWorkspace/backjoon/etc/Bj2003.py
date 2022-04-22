import sys


def solution():
    N, M = map(int,sys.stdin.readline().split())
    l = list(map(int,sys.stdin.readline().split()))
    # i 부터 j까지 의 합이 M 이 되는 지 확인해야 한다. 그럼 맨 처음 i부터 시작한다.
    i = 0
    N = 1
    ans = 0
    while(True):
        num = sum(l[i:i+N])
        # print(l[i:i+N])
        # print(num)
        if num==M:
            ans+=1
            i+=1
            N=1
        elif num<M:
            N+=1
        elif num>M:
            i+=1
            N = 1
        if i+N>len(l):
            break
        if(i>len(l)-1):
            break

    print(ans)

if __name__=="__main__":
    solution()