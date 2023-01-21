N: int = int(input())
list_size: int = int(input())

l = input()
dp = [0 for _ in range(list_size)]
word = "I"
word += "OI"*N
start = 0
for i in range(list_size):
    if l[i] == word[start]:
        start += 1
        if start == len(word):
            dp[i] = 1
            start = 0
    else:
        if l[i]==word[0]:
            start = 1
        else:
            start=0
for i in range(2, len(dp)):
    if dp[i - 2] == 1 and l[i - 1] == "O" and l[i] == "I":
        dp[i] = 1
print(sum(dp))
