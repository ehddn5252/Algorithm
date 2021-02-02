


if __name__=="__main__":
    N=input()
    numberList=[]
    for i in N:
        numberList.append(i)
    
    numberList.sort(reverse=True)

    answerStr=""
    for i in numberList:
        answerStr+=i
    print(answerStr)