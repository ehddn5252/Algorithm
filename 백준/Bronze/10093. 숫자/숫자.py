a, b = map(int, input().split(" "))
min_value = min(a,b)
max_value = max(a,b)
ans_num = max_value - min_value - 1
if max_value==min_value:
    ans_num=0
print(ans_num)
for i in range(min_value + 1, max_value):
    if i==b-1:
        print(i, end="")
    else:
        print(i,end=" ")
