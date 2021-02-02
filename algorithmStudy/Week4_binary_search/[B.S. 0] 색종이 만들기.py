# 작성일 : 20201119
# 작성자 : 김동우
# 문제명 : 색종이 만들기
# 문제 요약 : 2차원 배열이 주어진다. 각 2차원 배열의 전체 색이 같지 않으면 색종이를 1/4로 나눈다.
# 마지막으로 나눈 갯수를 구한다. 
#  

# 1 1|0 0
# 1 1|0 0
# --------
# 1 1|0 0
# 0 1|0 1

# 문제 해설 :
# 1. 배열 탐색을 한다. 만약 같은 수가 있을 경우


def input_Func():
    N=int(input())
    inputedList=[]

    for _ in range(N):
        inputedList=list(map(int,input().split()))
    return inputedList

#def recursive():


def solution(inputedList):
    for rowIndex,row in enumerate(inputedList):
        for colIndex,col in enumerate(inputedList):




if __name__ == "__main__":
    solution(input_Func())