T = int(input())

n1 = int(input())
l1 = list(map(int, input().split(" ")))

n2 = int(input())
l2 = list(map(int, input().split(" ")))

map1 = {}
# l1의 부 배열과 l2의 부 배열을 합해서 나올 수 있는 경우의 수를 구하기
dp = []
for i in range(n1):
    for j in range(i + 1):
        tmp = sum(l1[j:i + 1])
        map1.setdefault(tmp, 0)
        map1[tmp] += 1

ans = 0
for i in range(n2):
    for j in range(i + 1):
        tmp = sum(l2[j:i + 1])
        if map1.get(T - tmp):
            ans += map1.get(T - tmp)
print(ans)
