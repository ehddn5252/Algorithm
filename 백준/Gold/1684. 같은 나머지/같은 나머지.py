import sys


input()
l = list(map(int, sys.stdin.readline().split(" ")))
max_n = 1
for i in range(1,1001):
    r = -1
    for num in l:
        r_before = r
        r = num % i
        if r_before!=-1:
            if r!=r_before:
                break
    else:
        max_n = i
print(max_n)

