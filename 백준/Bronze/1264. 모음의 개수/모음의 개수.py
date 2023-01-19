l = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

while True:
    s = input()
    if s == "#":
        break
    ans = 0
    for i,t in enumerate(s):
        if t in l:
            ans += 1
    print(ans)
