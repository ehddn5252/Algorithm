# 작성일자 : 20210202
# 문제명 : 잃어버린 괄호
# 문제 풀이 :


from sys import stdin


def solution(inputedString):
    number=''
    for i in inputedString:
        if i>='0' and i<='9':
            number+='i'
        else:
            numberList.append(int(number))
            operator=i 

if __name__=="__main__":
    inputedString= stdin.readline().strip()
    solution(inputedString)