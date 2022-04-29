N,C = map(int,input().split(" "))  # 2<=N<=2000, 1<=c<=10000
bus_trunk = [0 for i in range(N+2)]
M = int(input())
l = []
for i in range(M):
    a, b, boxN = map(int,input().split(" "))
    l.append([a, b, boxN])

'''
1. 1번부터 차례로 마을을 가면서 물건을 배송한다.
2. 박스를 보내는 마을 번호, 받는 마을 번호와 보낼 박스의 개수를 알고 있다.
이 트럭 한대로 배송할 수 있는 최대 박스 수를 구하라.
// 방법으로는 DP, 

일단 마을 순서로 차례로 트렁크 용량을 채운다.
'''
sum_weight:int = 0
current_town = 1
ans = 0
# 첫 if 조건 요청을 위해 데이터를 더 넣는다.
for i in range(1, N+2):
    l.append([i,0,0])

l.sort(key=lambda x:[x[0],x[1]])
print(l)

for i,v in enumerate(l):
    if current_town != v[0]:
        current_town = v[0]
        ans += bus_trunk[current_town]
        sum_weight -= bus_trunk[current_town]
        bus_trunk[current_town] = 0
        print(ans)

    # 여기에서 더 가까이에 있는
    elif v[0] == current_town:
        for j, vj in enumerate(bus_trunk):
            '''
            1. 만약 뒤에 있는 애것이 앞에 실은 애꺼보다 크면 버리고 앞에 있는 애꺼 추가
            '''
            if(j<=i):
                continue
            if(v[2]>=vj) and v[2] + sum_weight:
                bus_trunk[j]

        if v[2]+sum_weight <= C and v[2] + sum_weight <= C:
            sum_weight += v[2]
            bus_trunk[v[1]] += v[2]
        elif sum_weight <= C and v[2] + sum_weight > C:
            bus_trunk[v[1]] += C-sum_weight
            sum_weight = C
    print(v, bus_trunk)
print(ans)