# 작성일 : 20201113
# 작성자 : 김동우
# 문제명 : 합이 0인 네 정수
# 문제요약 : 배열 4개를 A,B,C,D를 선택해서 A[0] + B[1] + C[2] + D[3] == 0 이되는 순서쌍 구하기


def solution(N):
    answer=0
    inputedList=[]
    for _ in range(N):
        inputedList.append(list(map(int,input().split())))
    
    inputedList.sort(key=lambda x:x[0])
    for list1 in inputedList:
        sumAnswer=sum(list1)
        print(sumAnswer)
        if sumAnswer==0:
            answer+=1

    print(answer)

if __name__ == "__main__":
    N=int(input())
    solution(N)