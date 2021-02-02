# 작성일자 : 20201228
# 작성자 : 김동우
# 문제명 : 셀프 넘버 (백준 4673번)
# 문제 요약 : 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.
# n을 d(n)의 생성자라 할 때(d(75)=87, 87의 생성자는 75) 생성자가 없는 수를 셀프 넘버라 한다.


def findSelfNumber(i):
    returnValue=i
    while i>0.99999:
        returnValue+=i%10
        i//=10
    if returnValue>10000:
        returnValue=0
    return int(returnValue)


def solution():
    a=[]
    a.append(0)
    for _ in range(1,10001):
        a.append(1)
    for i in range(1,10001):
        a[findSelfNumber(i)]=0
    
    for i in range(1,10001):
        if a[i]==1:
            print(i)

if __name__ == "__main__":
    solution()