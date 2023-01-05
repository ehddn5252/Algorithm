# 부분 합 중 합이 S 이상이 되는 것 중 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오
import math

N = int(input())
if N == 1:
    print(0)
    exit()

max_value = N + 1
l = [True for i in range(max_value)]
l[0] = False
l[1] = False
for i in range(2, int(math.sqrt(max_value) + 1)):
    if not l[i]:
        continue
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            l[i] = False
            break
    if i < int(math.sqrt(max_value)) + 1 and l[i]:
        start = 2
        while i * start < max_value:
            l[i * start] = False
            start += 1
start = 0
end = 0
prime = []
for i in range(len(l)):
    if l[i]:
        prime.append(i)

count = 0

sum_value = prime[end]
while start <= end < len(prime):
    if sum_value >= N:
        while True:
            if sum_value == N:
                count += 1
                sum_value -= prime[start]
                start += 1
                break
            elif sum_value > N:
                sum_value -= prime[start]
                start += 1
            elif sum_value < N:
                break
    if sum_value < N:
        if end + 1 == len(prime):
            break
        end += 1
        sum_value += prime[end]

print(count)
