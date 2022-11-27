nums = [ 0 for i in range(31)]
for i in range(28):
    num = int(input())
    nums[num]=1

for i in range(1,31):
    if nums[i]!=1:
        print(i)