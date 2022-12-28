from sys import stdin

if __name__=="__main__":
    testcase= int(stdin.readline())
    dp=[0 for _ in range(12)]
    dp[0]=1
    dp[1]=1
    dp[2]=2
    for i in range(3,12):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    for i in range(testcase):
        number=int(stdin.readline())
        print(dp[number])