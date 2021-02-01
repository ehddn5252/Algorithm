import time
import math

'''
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
'''
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