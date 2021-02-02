# 작성 일자 : 20201228
# 작성자 : 김동우
# 문제명 : 사분면 고르기
# 문제 요약 : x좌표, y좌표가 주어진다. 좌표에 따른 사분면을 출력하라.

# 문제 풀이 : 
# 1. 1사분면은 x : +, y : +
# 2. 2사분면은 x : -, y : +
# 3. 3사분면은 x : -, y : -
# 4. 4사분면은 x : +, y : - 


def solution():
    x = int(input())
    y = int(input())
    if x>0 and y > 0:
        print(1)
    elif x<0 and y > 0:
        print(2)
    elif x<0 and y < 0:
        print(3)
    elif x>0 and y < 0:
        print(4)


if __name__ == "__main__":
    solution()
    
