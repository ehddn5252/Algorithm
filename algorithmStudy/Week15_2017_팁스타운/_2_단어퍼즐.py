# 문제 풀이 : dp
# 1. 문자열의 개수만큼 dp 배열을 만든다.
# 2. 처음부터 찾아보는데 단어 조각의 길이가 최대 5개이다.
# 3. dp 배열을 t(target string)의 크기 +1만큼 만들고 dp[0]은 0으로 나머지는 값을 무한대로 초기화한다.
# 4. 이제 for문에 들어가서 strs에 단어가 있는 지 확인한다. 
def solution(strs, targetWord):
    n=len(targetWord)
    dp=[9876543210]*(n+1)
    dp[0]=0
    strs=set(strs)
    for dpIndex in range(1,n+1):
        # strs에 있는 단어의 길이가 최대 5임으로 
        for wordLength in range(1,6):
            if dpIndex-wordLength>=0:
                string1=dpIndex-wordLength
            else:
                string1=0
            if targetWord[string1:dpIndex] in strs:
                dp[dpIndex]=min(dp[dpIndex],dp[string1]+1)

    if dp[-1]==9876543210:
        return -1
    else:
        return dp[-1]