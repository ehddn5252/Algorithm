num = int(input())
str1 = ""
all_len = []
for i in range(num):
    tmp = input()
    if i == 0:
        for j in range(len(tmp)):
            all_len.append(tmp[j])
        str1 = tmp
    for i, tmp_i in enumerate(tmp):
        if all_len[i] != tmp_i:
            all_len[i]='?'

print("".join(all_len))