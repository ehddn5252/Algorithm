



def isPrimeNumber(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
    

if __name__=="__main__":
    start= int(input())
    end= int(input())
    answer=0
    numSum=0
    minimum=0
    for num in range(start,end+1):
        if(isPrimeNumber(num) and num!=1):
            if numSum==0:
                minimum=num
            numSum+=num

    if numSum==0:
        print(-1)
    else:
        print(numSum)
        print(minimum)