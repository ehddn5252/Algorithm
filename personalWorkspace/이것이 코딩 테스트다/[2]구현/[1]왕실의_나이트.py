# 작성일자 : 20210204
# 문제명 : 왕실의 나이트
# 문제 요약 :
# 나이트는
# 1. 수평으로 두 칸 이동 후 수직으로 한 칸 또는 
# 2. 수직으로 두 칸 이동 후 수평으로 한 칸 이동 가능하다. 나이트가 이동할 수 있는 경우의 수를 구하시오

# 여기서 팁은 row와 column을 각각 미리 구하는 것
import sys







def solution(inputStr):
    row = int(inputStr[1])
    column=int(ord(inputStr[0]))-int(ord('a'))+1
    steps = [(-2,1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column=column+step[1]
        if next_row>=1 and next_row <=8 and next_column >=1 and next_column <=8:
            result+=1
    print(result)

if __name__=="__main__":
    inputStr=sys.stdin.readline().strip()
    solution(inputStr)