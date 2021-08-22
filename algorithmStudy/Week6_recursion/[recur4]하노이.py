# 작성일자 : 20210101
# 작성자 : 김동우
# 문제명 : 하노이
# 문제 풀이 : 하노이 움직인 횟수 구하기
# 문제 해석 :
# 1. 맨 밑에 있는 원판을 목적지로 옮겨야한다.
# 2. 그래서 그 위에 있는 것들을 경유지로 옮겨야 한다.
# 3. 그리고 맨 밑에 있는 원판을 목적지로 옮겼다면 그 위에 있던
# 4. 경유지에 있던 것들을 목적지로 옮겨야 한다.


def move(N, start, to):
    print(str(start)+" "+str(to))


def hanoi(N, start, to, via):
    if N == 1:
        move(1, start, to)
    else:
        hanoi(N-1, start, via, to)
        move(N, start, to)
        hanoi(N-1, via, to, start)

if __name__ == "__main__":
    n=int(input())
    print(2**n-1)
    hanoi(n,1,3,2)
    