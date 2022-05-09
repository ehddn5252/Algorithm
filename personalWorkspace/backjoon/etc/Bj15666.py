from itertools import product
n,m = map(int,input().split(" "))
n_list = list(set(map(int,input().split(" "))))
n_list.sort()
new_list = []
for i in product(n_list,repeat=m):
    continue_flag = False
    first = i[0]
    for index,value in enumerate(i):
        if value<first:
            continue_flag=True
            break
        first=value
    if(continue_flag):
        continue

    if i not in new_list:
        new_list.append(i)

for inner_list in new_list:
    for i in inner_list:
        print(str(i)+" ", end="")
    print("")