from sys import stdin
dp=[0]*100000
def solution():
	global coinList, K
	for coin in coinList:
		dp[coin]+=1
		for index in range(coin+1,K+1):
			dp[index]+=dp[index-coin]
	print(dp[K])



if __name__=="__main__":
    global coinList, K
    N,K=map(int,stdin.readline().split())
    coinList=[]
    for i in range(N):
        coinKind=int(stdin.readline())
        if coinKind<=K:
            coinList.append(coinKind)
    solution()