import sys


# sys.stdin.readline()을 사용하지 않으면 시간초과가 난다.
if __name__=="__main__":
    N=int(input())
    numberList=[]
    for i in range(N):
        numberList.append(list(map(int,sys.stdin.readline().split())))
    numberList.sort(key=lambda x:(x[1],x[0]))

    for i in numberList:
        print(str(i[0])+" "+str(i[1]))