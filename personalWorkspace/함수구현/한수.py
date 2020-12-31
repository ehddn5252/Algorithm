# 작성일자 : 20201228
# 작성자 : 김동우
# 문제명 : 한수 
# 문제 요약 : 각 자리의 수가 등차수열을 이루면 한수라고 한다. 입력값 n이 주어졌을 때 n이하의 한수의 개수를 구하시오


import sys

def findHanNumber(i):
    # 53 이면 first 가 3 second 가 5
    first=i%10
    second=(i//10)%10
    onedifference=first-second
    returnValue=True
    if i<100:
        return True
    while i>=10:
        saveOne=i%10
        i//=10
        saveTwo=i%10
        difference=saveOne-saveTwo
        if onedifference!=difference:
            returnValue=False
            break
    return returnValue

def solve():
    intValue=int(sys.stdin.readline())
    ans=0
    for i in range(1,intValue+1):
        if (findHanNumber(i)):
            ans+=1
    print(ans)


if __name__ == "__main__":
    solve()