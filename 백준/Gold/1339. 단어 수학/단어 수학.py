n = int(input())
numbers = [i for i in range(9, -1, -1)]
dict1 = {}
for i in range(n):
    alphabets = input()
    for j, v in enumerate(alphabets):
        dict1.setdefault(v, 0)
        dict1[v] += 10 ** (len(alphabets) - j - 1)

ans = 0
for i, v in enumerate(sorted(dict1.values(), reverse=True)):
    ans += numbers[i] * v
print(ans)
