import sys

# 문제 테스트케이스가 틀릴 때 생각해야할 것 :
# 1. 입력의 범위
# 2. 초기 조건 
# 3. 점화식
# 4. 원하는 출력  
def solution(stairs):
    dp=stairs[:]
    dp[1]=stairs[0]+stairs[1]
    dp[2]=max(stairs[0]+stairs[2],stairs[1]+stairs[2])
    for index in range(3,len(stairs)):
        dp[index]= max(dp[index-3]+stairs[index-1]+stairs[index],dp[index-2]+stairs[index])
    print(dp[-1])


if __name__=="__main__":
    step=int(sys.stdin.readline())
    stairs=[]
    
    for i in range(step):
        stairs.append(int(sys.stdin.readline()))
    if step==1:
        print(stairs[0])
    elif step==2:
        print(stairs[0]+stairs[1])
    else:
        solution(stairs)