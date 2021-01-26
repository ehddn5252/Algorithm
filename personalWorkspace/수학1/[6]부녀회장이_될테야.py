import math
if __name__=="__main__":
    
    testcase=int(input())
    # 14행 5열
    dp=[[0]*(14)  for _ in range(15)]
    dp[0]=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

    for i in range(1,15):
        for j in range(len(dp[0])):
            dp[i][j]=sum(dp[i-1][:j+1])
    for _ in range(testcase):
        floor=int(input())
        room=int(input())-1
        # room은 1호부터 시작하니까 맞춰주기 위해서 1을 뺀다
        print(dp[floor][room])
