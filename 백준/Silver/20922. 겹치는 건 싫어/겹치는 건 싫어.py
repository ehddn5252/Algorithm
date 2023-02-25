"""
1. 포인터 2개를 잡습니다.
2. 현재 가장 개수가 많은 데이터와 방금 넣은 데이터의 개수를 비교해서 max개수 데이터를 정합니다.
3. max_num 데이터의 값이 k개 이하라면 end+=1 해서 리스트를 더해갑니다.
4. max_num 데이터의 값이 k개를 넘기면 start+=1 해서 해당 값을 줄여갑니다. 
"""
import sys

N, K = map(int, input().split(" "))
l = list(map(int, sys.stdin.readline().split(" ")))

start = 0
end = 0

map1 = {-1: 0}
max_value_index = -1
max_value_num = 0
ans = 0
while len(l) > end >= start:

    if map1[max_value_index] <= K:
        map1.setdefault(l[end], 0)
        map1[l[end]] += 1
        if map1[l[end]] > map1[max_value_index]:
            max_value_index = l[end]
        end += 1
        ans += 1
        if map1[max_value_index] > K:
            continue
        if max_value_num < ans:
            max_value_num = ans
    else:
        map1[l[start]] -= 1
        ans -= 1
        start += 1

print(max_value_num)
