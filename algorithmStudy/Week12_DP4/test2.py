# 파일 합치기 참고 블로그(https://suri78.tistory.com/15)
# 참고 유튜브 (https://www.youtube.com/watch?v=4OdIDIYLHlY)
# 이해 안되노;;
# 연속된 두 파일을 합쳐야 한다.
import sys


def solution(num,page):
    table = [[0]*num for _ in range(num)]
    for col in range(1,num):
        for row in range(col-1,-1,-1):
            minValue = 9876543210
            for k in range(col-row):
                minValue=min(minValue,table[row][row+k]+table[row+k+1][col])
            table[row][col]= minValue+sum(page[row:col+1])
    print(table[0][num-1])


if __name__=="__main__":
    testcase= int(sys.stdin.readline())
    for _ in range(testcase):
        num=int(sys.stdin.readline())
        page=list(map(int,sys.stdin.readline().split()))
        solution(num,page)
