# Fly me to the Alpha Centauri
# 
def solution():
    x,y= map(int,input().split())
    # 1 : (1개)
    # 1 1 : 2 (2개)
    # 1 1 1 : 3 : (3개)
    # 1 2 1  : 4 : (3개)
    # 1 2 2 1 : 6 : (4개)
    # 1 2 3 2 1 : 9 (5개)
    # 1 2 3 3 2 1 : 12
    # 1 2 3 4 3 2 1 : 16
    # 1 2 3 4 4 3 2 1 : 20
    # 1 2 3 4 5 4 3 2 1 : 25
    # 1부터 4까지 제외하고 4부터 개수가 바뀔 때 이전 수와의 차이가 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 이다. 즉 규칙적이다.
    # 그래서 초기조건 예외처리 후 일반화 식을 만들면 된다.
    distance=y-x
    if distance==1:
        print(1)
    elif distance==2:
        print(2)
    elif distance==3 or distance==4:
        print(3)
    else:
        oddEven=1
        i=2
        answer=3
        while distance-4>0:
            if oddEven%2==0:
                i+=1
            distance-=i
            oddEven+=1
            answer+=1
        print(answer)
        
if __name__=="__main__":
    testcase=int(input())
    for i in range(testcase):
        solution()