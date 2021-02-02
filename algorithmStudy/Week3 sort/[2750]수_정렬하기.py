if __name__=="__main__":
    N=int(input())
    numberList=[]
    for i in range(N):
        number=int(input())
        numberList.append(number)
    numberList.sort()

    for number in numberList:
        print(number)
