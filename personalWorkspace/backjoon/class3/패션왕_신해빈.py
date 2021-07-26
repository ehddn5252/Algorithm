# 작성일자 : 20210302

import sys

if __name__=="__main__":
    testCase=int(sys.stdin.readline())
    for i in range(testCase):
        inputNum=int(sys.stdin.readline())
        clothHash={}
        for i in range(inputNum):
            inputedString=sys.stdin.readline()
            for index,value in enumerate(inputedString):
                if value==" ":
                    inputedString=inputedString[index+1:]
                    break
            if clothHash.get(inputedString,0)==0:
                clothHash[inputedString]=1
            else:
                clothHash[inputedString]+=1
        answer=1
        for value in clothHash.values():
            answer*=value+1
        print(f'{answer-1}')
