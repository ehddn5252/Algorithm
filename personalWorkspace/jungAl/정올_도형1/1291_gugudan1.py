n=0
m=0
while(n<2 or n>9 or m<2 or m>9):
    n, m = map(int, input().split(" "))
    if((n<2 or n>9) or (m<2 or m>9)):
        print("INPUT ERROR!")

def calc(n,m):
    for i in range(1, 10):
        if n>m:
            for j in range(n,m-1,-1):
                if(j!=m):
                    print(f"{j} * {i} ={str(j * i).rjust(3)}"+"   ",end="")
                else:
                    print(f"{j} * {i} ={str(j * i).rjust(3)}" + " ")
        else:
            for j in range(n,m+1):
                if (j != m):
                    print(f"{j} * {i} ={str(j * i).rjust(3)}" + "   ", end="")
                else:
                    print(f"{j} * {i} ={str(j * i).rjust(3)}" + " ")

calc(n,m)