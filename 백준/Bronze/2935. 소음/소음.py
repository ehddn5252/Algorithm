a = input()
oper = input()
b = input()

if oper == "*":
    ans = "1" + "0" * (len(a) - 2 + len(b))
    print(ans)
else:
    if a==b:
        ans = "2" + "0"*(len(a)-1)
    else:
        max_value = max(len(a), len(b))
        min_value = min(len(a), len(b))
        ans = "1"
        for i in range(max_value-1):
            if i == max_value - min_value-1:
                ans += "1"
            else:
                ans += "0"
    print(ans)
