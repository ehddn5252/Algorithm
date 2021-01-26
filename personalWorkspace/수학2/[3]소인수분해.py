#import time

def isPrimeNumber(num):
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True


if __name__=="__main__":
    num= int(input())
    #start = time.time()
    answer=[]
    while num>1:
        for i in range(2,num+1):
            if num%i==0 and isPrimeNumber(i):
                answer.append(i)
                num//=i
                break
    answer.sort()
    for number in answer:
        print(number)
    #print("time :", time.time() - start)