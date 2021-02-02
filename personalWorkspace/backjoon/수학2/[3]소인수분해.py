#import time
'''
문제
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
'''

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