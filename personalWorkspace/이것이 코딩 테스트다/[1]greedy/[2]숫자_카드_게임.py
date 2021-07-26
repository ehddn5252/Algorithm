# 작성일자 : 20210202
# 문제명 : 숫자 카드 게임
# 문제 요약 :
# 각 행 중의 가장 작은수 들 중 가장 큰 수를 찾는 문제
import sys

def solution(matrix):
    answer=-99999
    for col in matrix:
        if answer<min(col):
            answer=min(col)
    print(answer)
    
    
if __name__=="__main__":
    matrix=[]
    col,row= map(int,sys.stdin.readline().split())
    for i in range(col):
        
        numList=list(map(int,sys.stdin.readline().split()))
        matrix.append(numList)
    solution(matrix)

    