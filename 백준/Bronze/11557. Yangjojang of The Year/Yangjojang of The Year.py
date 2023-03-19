testcase = int(input())

for _ in range(testcase):
    map1 = {}
    n = int(input())
    for _ in range(n):
        a, b = map(str, input().split(" "))
        map1.setdefault(a, 0)
        map1[a] += int(b)
    max_value=0
    ans=""
    for k,v in map1.items():
        if int(v)>max_value:
            max_value=int(v)
            ans=k
    print(ans)