n,weights = int(input()), list(map(int,input().split()))
m,marbles = int(input()), list(map(int,input().split()))

dp = [ [0 for i in range((i+1)*500+1)] for i in range(n+1)]

def power_set(num,weight):
    # 추 다 돌으면 return
    if num > n:
        return

    # 방문 했으면 return
    if dp[num][weight]:
        return

    # 방문 처리를 한다.
    dp[num][weight]=1

    # 추의 개수 별로 될 수 있는 형태가 가능한 지 모두 확인 해준다. 이렇게 되면 추의 개수별 해당 무게를 잴 수 있는 지 확인 가능하다.
    # 현재 무게
    power_set(num+1,weight)
    # 더한 무게
    power_set(num+1,weight+weights[num-1])
    # 뺀 무게
    power_set(num+1,abs(weight-weights[num-1]))



power_set(0,0)

for marble in marbles:

    if marble > 30*500:
        print("N")
    elif dp[n][marble]==1:
        print("Y")
    else:
        print("N")