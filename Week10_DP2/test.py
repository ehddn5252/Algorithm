
def solution(str1,str2):
    str1Len=len(str1)
    str2Len=len(str2)

    dp=[[0]*(str2Len+1)  for _ in range(str1Len+1)]
    for i in range(1,str1Len+1):
        for j in range(1,str2Len+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    
    print(dp[-1][-1])


if __name__=="__main__":
    str1=input()
    str2=input()
    solution(str1,str2)