m, s = map(int, input().split(" "))
dp = [-1] * 101
dic = {}
for _ in range(m+s):
    k, v = map(int,input().split(" "))
    dic[k] = v

q = []

for i in range(2,8):
    if i in dic:
        dp[dic[i]]=1
        q.append(dic[i])
    else:
        dp[i]=1
        q.append(i)

dp[0]=0
dp[1]=0
while q:
    popped = q.pop(0)
    if popped == 100:
        print(dp[100])
        break
    for i in range(1,7):
        if 1<=popped+i <=100:
            if popped+i not in dic:
                if dp[popped+i] == -1 or dp[popped + i]> dp[popped]+1:
                    q.append(popped+i)
                    dp[popped+i] = dp[popped]+1
            else:
                dic_value = dic[popped + i]
                if dp[dic_value]==-1 or dp[dic_value]>dp[popped]+1:
                    q.append(dic_value)
                    dp[dic_value] = dp[popped] + 1
