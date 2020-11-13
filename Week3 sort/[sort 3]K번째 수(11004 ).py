# 작성일 : 20201113
# 작성자 : 김동우
# 문제명 : K번째 수
# 문제요약 : N,K가 주어지고 둘째줄에는  수가 주어진다.
#  정렬했을 떄 앞에서부터 K번째 수를 출력 
# 


def solution(N,K):
    inputedList=[]
    inputedList=list(map(int,input().split()))
    inputedList.sort()
    print(inputedList[K-1])

if __name__ == "__main__":
    N,K=map(int,input().split())
    solution(N,K)