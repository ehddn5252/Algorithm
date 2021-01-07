from itertools import permutations

# 문제명: N 과 M
# 문제 요약 : n과 m이 주어진다. n가지 수 중 반복이 포함되지 않게 m개를 뽑는 경우의 수를 구하라 (순서가 상관이 있다)
# 문제 풀이 :
# 1. 그냥 순열이다 순열 라이브러리 써서 순열을 구한다


def solution():
    n,m= map(int,input().split())
    numList=[]
    for num in range(1,n+1):
        numList.append(num)
    ans=""
    per = list(permutations(numList,m))
    for numTuple in per:
        for num in numTuple:
            ans+=str(num)+" "
        print(ans)
        ans=""

if __name__ == "__main__":
    solution()