n = int(input())
s = input()

l = ['000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010']
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def check(ss):
    ans = ""
    for i, alphabet in enumerate(l):
        check_num = 0
        for j, ss_inner in enumerate(ss):
            if alphabet[j] != ss[j]:
                check_num += 1
        if check_num > 1:
            continue
        else:
            return alphabets[i]
    return "X"


ans = ""
for i in range(0, n * 6, 6):
    tmp = check(s[i:i + 6])
    if tmp == "X":
        print((i // 6) + 1)
        exit(0)
    else:
        ans += tmp

print(ans)