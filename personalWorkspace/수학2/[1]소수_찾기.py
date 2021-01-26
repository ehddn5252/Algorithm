



def isPrimeNumber(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
    

if __name__=="__main__":
    _=int(input())
    numbers= list(map(int,input().split()))
    answer=0
    for num in numbers:
        if(isPrimeNumber(num) and num!=1):
            answer+=1
    print(answer)