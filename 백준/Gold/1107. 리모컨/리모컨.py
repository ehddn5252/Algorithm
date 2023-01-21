target: int = int(input())
N: int = int(input())
l=[]
if N!=0:
    l = list(map(int, input().split(" ")))

min_num = abs(100-target)

for n in range(1000001):
    digit_check = str(n)

    for j in range(len(digit_check)):
        if int(digit_check[j]) in l:
            break
        elif j==len(digit_check)-1:
            min_num = min(min_num,abs(n - target)+len(digit_check))
print(min_num)