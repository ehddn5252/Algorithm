import sys


def solution():
    # N은 안쓰임
    N = int(sys.stdin.readline())
    l = list(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    for i in range(M):
        isEqual = True
        # 2,5 면 3.5 2,3인데
        start, end = map(int,sys.stdin.readline().split())
        start = start-1
        for i in range(start,int((start+end)/2)):
            # print("=========")
            # print(i,end - i + start - 1)
            # print(l[i], l[end - i + start - 1])
            # print("=========")
            if(l[i]!=l[end - i + start - 1]):
                isEqual = False
                print(0)
                break
        if(isEqual):
            print(1)


if __name__=="__main__":
    solution()