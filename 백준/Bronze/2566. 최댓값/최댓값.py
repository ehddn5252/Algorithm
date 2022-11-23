max_value = 0
ans_x=0
ans_y=0
for i in range(9):
    tmp = list(map(int, input().split(" ")))
    for j in range(len(tmp)):
        if tmp[j] > max_value:
            max_value = tmp[j]
            ans_x = i
            ans_y = j
print(max_value)
print(str(ans_x+1)+" "+str(ans_y+1))



