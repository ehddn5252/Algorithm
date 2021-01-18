def solution(m, n, puddles):
    dp=[]
    for i in range(n):
        sample=[]
        for i in range(m):
            sample.append(1)
        dp.append(sample)
    # 초기조건
    for puddle in puddles:
        dp[puddle[1]-1][puddle[0]-1]=0
        if puddle[1]-1==0 :
            for i in range(len(dp[0])):
                if i>puddle[0]-1:
                    dp[0][i]=0
        elif puddle[0]-1==0 :
            for i in range(len(dp)):
                if i>puddle[1]-1:
                    dp[i][0]=0
    # dp 배열 만들기
    for rowIndex,rowValue in enumerate(dp):
        if rowIndex==0: continue
        for colIndex,colValue in enumerate(rowValue):
            if colIndex==0: continue
            if dp[rowIndex][colIndex]!=0:
                dp[rowIndex][colIndex]=dp[rowIndex-1][colIndex]+dp[rowIndex][colIndex-1]
    print(dp)
    return dp[-1][-1]%1000000007