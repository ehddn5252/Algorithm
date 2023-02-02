# 랜선 개수, 필요한 랜선 개수
K, N = map(int, input().split(" "))
l = []

for _ in range(K):
    l.append(int(input()))

l.sort()

start = 1
end = l[-1]
cable_num=0
while start<=end:
    '''
    등분할 길이가 mid가 된다.
    등분할 길이가 크면 케이블 개수가 적어진다.
    그래서 케이블 개수가 많으면 등분할 길이를 크게해야 한다.
    '''
    mid = (start + end) // 2
    cable_num = 0
    for i in range(len(l)):
        cable_num += l[i] // mid
    if cable_num >= N:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)