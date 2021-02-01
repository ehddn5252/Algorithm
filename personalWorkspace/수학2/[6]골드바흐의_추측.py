import time
import math
'''
문제
1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

출력
각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.
'''

# 소수이면 False인 에라토스테네스의 채
def mkSieveOfEratosthenes(sieveOfEratosthenes):
    sieveOfEratosthenes[0]=True
    sieveOfEratosthenes[1]=True
    for i in range(2,int(math.sqrt(10000))+1):
        if sieveOfEratosthenes[i]==False:
            j=2
            while i*j<10000:
                # 소수이면 False
                sieveOfEratosthenes[i*j]=True
                j+=1
    return sieveOfEratosthenes[:]

if __name__=="__main__":
    testcase=int(input())
    sieveOfEratosthenes=[False]*10000
    primeNumbers=[]
    primeNumbers=mkSieveOfEratosthenes(sieveOfEratosthenes[:])

    for _ in range(testcase):
        number=int(input())
        answer=[0,0]
        minValue=10000
        for i in range(2,number//2+1):
            if primeNumbers[i]==False and primeNumbers[number-i]==False and abs(number-2*i)<minValue:
                minValue=abs(number-2*i)
                answer[0]=i
                answer[1]=number-i
        strAns=str(answer[0])+" "+str(answer[1])
        print(strAns)
                


