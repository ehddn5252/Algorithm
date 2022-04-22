import sys



# 질문이 100만번이라서 다른 방법을 사용해야 한다.
# dp 를 사용해서 미리 다 계산을 해놓는다.
def solution():
    # N은 안쓰임
    N = int(sys.stdin.readline())
    l = list(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    dp = [[[]for i in range(2000)] for i in range( 2000)]
    for i in range(M):
        isEqual = True
        start, end = map(int,sys.stdin.readline().split())
        start = start-1


if __name__=="__main__":
    solution()


