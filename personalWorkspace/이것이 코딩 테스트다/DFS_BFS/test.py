# 작성일자 : 20210205
# 문제명 : 음료수 얼려 먹기
# 문제 요약 : N x M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라
# 

from sys import stdin




def solution(iceFrame):
    print(1)
    
if __name__=="__main__":
    row,col = map(int,stdin.readline().split())
    iceFrame=[]
    visited=[ [0]*col for _ in range(row)]
    print(visited)

    for _ in range(row):
        iceFrame.append(list(map(int,stdin.readline().split())))
    
    solution(iceFrame)

