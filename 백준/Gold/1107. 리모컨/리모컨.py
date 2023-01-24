target: int = int(input())
N: int = int(input())
l = []
if N != 0:
    l = list(map(int, input().split(" ")))

min_value = abs(100-target)
for i in range(1000001):
    digit = str(i)
    for j in range(len(digit)):
        if int(digit[j]) in l:
            break
        elif j == len(digit) - 1:
            min_value = min(min_value, abs(i - target) + len(digit))
print(min_value)
