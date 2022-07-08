
def case1(num):
    for i in range(1,num+1):
        for j in range(num):
            print(str(i)+" ",end="")
        print("")

def case2(num):
    for i in range(1,num+1):
        if(i%2==1):
            for j in range(1, num+1):
                print(str(j)+" ",end="")
        else:
            for j in range(num,0,-1):
                print(str(j)+" ",end="")
        print("")

def case3(num):
    for i in range(1,num+1):
        for j in range(1,num+1):
            print(str(i*j)+" ",end="")
        print("")

n, m = map(int, input().split(" "))

if m == 1:
    case1(n)
elif m == 2:
    case2(n)
else:
    case3(n)

