N,K = map(int,input().split(" "))
now=0
break_flag=False
for i in range(1,N+1):
    if N%i==0:
        now+=1
    if now==K:
        print(i)
        break_flag=True
        break

if not break_flag:
    print(0)