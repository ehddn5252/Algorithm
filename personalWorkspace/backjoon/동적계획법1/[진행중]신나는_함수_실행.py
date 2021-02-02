'''
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
'''
import sys
# 딱 보아하니 abc 2차배열 각이네
# -> 3차원 배열로 해야한다.



def printABC(a,b,c,answer):
    print("w("+a+", "+b+", "+c+") = "+answer)


def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a > 20 or b > 20 or c >20:
        return 
    elif 




if __name__=="__main__":
    dp = [[[0 for col in range(21)] for row in range(21)] for depth in range(21)]
    while True:
        a,b,c=map(int,sys.stdin.readline().split())
        if a==-1 and b== -1 and c== -1:
            exit()
        else:
            if a<=0 or b<=0 or c<=0:
                answer=1
                printABC(a,b,c,answer)
            elif  a > 20 or b > 20 or c >20:
                printABC(a,b,c,answer)
            elif a<b and b<c:
                w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
            else:
                w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)