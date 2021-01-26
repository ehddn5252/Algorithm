import time
import math

if __name__=="__main__":
    #startTime=time.time()
    #print("time : "+str(time.time()-startTime))
    start,end= map(int,input().split())
    
    sieveOfEratosthenes=[False]*1000001
    sieveOfEratosthenes[0]=True
    sieveOfEratosthenes[1]=True
    for i in range(2,int(math.sqrt(end))+1):
        if sieveOfEratosthenes[i]==False:
            j=2
            while i*j<1000000:
                sieveOfEratosthenes[i*j]=True
                j+=1

    for index in range(start,end+1):
        if sieveOfEratosthenes[index]==False:
            print(index)