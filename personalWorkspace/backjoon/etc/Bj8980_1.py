N,C = map(int,input().split(" "))  # 2<=N<=2000, 1<=c<=10000

bus_trunk = [0 for i in range(N+1)]
M = int(input())
l = []
for i in range(M):
    a, b, boxN = map(int,input().split(" "))
    l.append([a-1, b-1, boxN])

ans = 0
# 가장 많이 적재된 박스 양을 구하고 여기에 더 추가할 수 있는 양을 구한다.
l.sort(key=lambda x:[x[1],x[0]])
for i,v in enumerate(l):
    boxN=0
    for j in range(l[i][0], l[i][1]):
        boxN = max(boxN, bus_trunk[j])

    current_weight = min(l[i][2], C-boxN)
    ans += current_weight
    for j in range(l[i][0], l[i][1]):
        bus_trunk[j] += current_weight

print(ans)