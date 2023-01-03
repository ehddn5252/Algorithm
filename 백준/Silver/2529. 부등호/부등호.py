from itertools import permutations

n = int(input())
operators = list(map(str, input().split(" ")))
numbers = [i for i in range(0, 10)]


def check(nums):
    global operators
    first = nums[0]
    for i, (num, operator) in enumerate(zip(nums[1:], operators)):
        if (operator == '>' and first > num) or (operator == "<" and first < num):
            first = num
        else:
            return False
    return True


max_value = 0
min_value = 9999999999
for i in permutations(numbers, n + 1):
    if check(i):
        tmp = int("".join(map(str, i)))
        max_value = max(max_value, tmp)
        min_value = min(min_value, tmp)

print(str(max_value).rjust(n + 1, "0"))
print(str(min_value).rjust(n + 1, "0"))
