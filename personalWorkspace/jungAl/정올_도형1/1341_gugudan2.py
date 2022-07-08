n=0
m=0
while(n<2 or n>9 or m<2 or m>9):
    n, m = map(int, input().split(" "))
    if((n<2 or n>9) or (m<2 or m>9)):
        print("INPUT ERROR!")

def calc(n,m):
    if n > m:
        for j in range(n, m - 1, -1):
            for i in range(1, 10):
                if(i%3!=0):
                    print(f"{j} * {i} ={str(j * i).rjust(3)}"+"   ",end="")
                else:
                    print(f"{j} * {i} ={str(j * i).rjust(3)}")
            print()
    else:
        for j in range(n,m+1):
            for i in range(1, 10):
                if(i%3!=0):
                    print(f"{j} * {i} ={str(j * i).rjust(3)}" + "   ", end="")
                else:
                    print(f"{j} * {i} ={str(j * i).rjust(3)}" + " ")
            print()

calc(n,m)