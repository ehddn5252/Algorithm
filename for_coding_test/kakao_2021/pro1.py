"""
남은 시간 04:30
1. 10진수를 n 진수로 바꾸는 함수
2. 0을 기준으로 split하는 문장
3. prime 인지 확인하는 문장

요약
n진수로 바꾸고 0을 기준으로 split하며
이게 소수인지 확인한다.

n진수로 바꾸려면?
"""
import math
def converter(n,k):
    converted_num:str=""
    quotient:int = n
    
    while True:
        if quotient<k:
            converted_num+=str(quotient)
            break
        remainder = quotient%k
        converted_num +=str(remainder)
        quotient//=k
    converted_num = list(converted_num)
    converted_num.reverse()
    converted_num =''.join(converted_num)
    return converted_num

def is_prime(num):
    check=0
    for i in range(2, math.sqrt(num+1)):
        if num/i==0:
            check+=1
    if check==0:
        return True
    else:
        return False

def solution(n, k):
    converted_string:str = converter(n,k)
    splited_nums=[map(int,converted_string.split("0"))]
    for i in splited_nums:if 
                   answer = -1
    return answer