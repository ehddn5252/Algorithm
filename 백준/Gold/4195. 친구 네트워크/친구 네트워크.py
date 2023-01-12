def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]


def merge(u, v):
    global friend_nums
    u = find(u)
    v = find(v)

    if u > v:
        parent[u] = v
        friend_nums[v] += friend_nums[u]
        friend_nums[u] = 1
        return friend_nums[v]
    elif u<v:
        parent[v] = u
        friend_nums[u] +=friend_nums[v]
        friend_nums[v] = 1
        return friend_nums[u]
    else:
        return friend_nums[u]

import sys
sys.setrecursionlimit(20000)

testcase = int(input())

for _ in range(testcase):
    map1 = {}
    parent = []
    N = int(sys.stdin.readline())
    friend_nums = [1 for _ in range(N*2)]
    num = 0
    for i in range(N):
        a, b = map(str, input().split(" "))
        if a not in map1.keys():
            map1[a] = num
            parent.append(num)
            num += 1
        if b not in map1.keys():
            map1[b] = num
            parent.append(num)
            num += 1
        print(merge(map1[a], map1[b]))
