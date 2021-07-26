# 작성 일자 : 20210312
# 문제명 : 수식 최대화
# 문제 요약 : 3가지 연산문자
# 1. 3가지 연산문자가 있다. + - *
# 2. 3가지 연산문자의 우선순위를 정해서
# 3. 가장 큰 값이 되는 경우를 return해야 한다. 
# 연산자 경우의 수 6개
# + > - > *
# + > * > -
# - > + > *
# - > * > +
# * > - > +
# * > + > -
import copy

def expressionCalcu(expressionList1,operateOrder,number):
    #print(expressionList1)
    while(operateOrder[number] in expressionList1):
        for index,_ in enumerate(expressionList1):
            if index+1<len(expressionList1):
                operater=expressionList1[index+1]
                if operater==operateOrder[number]:
                    if operater=="*":
                        expressionList1[index]=expressionList1[index]*expressionList1[index+2]
                    elif operater=="+":
                        expressionList1[index]=expressionList1[index]+expressionList1[index+2]
                    elif operater=="-":
                        expressionList1[index]=expressionList1[index]-expressionList1[index+2]
                    expressionList1.pop(index+1)
                    expressionList1.pop(index+1)
                    break
    return expressionList1


def solution(expression):
    answerList = []
    firstIndex=0
    
    expressionOperatelist=[["+","-","*"],["+","*","-"],["-","+","*"],["-","*","+"],["*","-","+"],["*","+","-"]]
    # exrpeesion에 리스트 형태로 저장한다.
    # "100-200*300-500+20"
    expressionList=[]
    for index,value in enumerate(expression):
        # 맨 마지막 일때
        if index==len(expression)-1:
            expressionList.append(int(expression[firstIndex:index+1]))

        if value=="-" or value=="*" or value=="+":
            expressionList.append(int(expression[firstIndex:index]))
            expressionList.append(expression[index])
            firstIndex=index+1
    print(expressionList)

    for operateOrder in expressionOperatelist:
        expressionList1=copy.deepcopy(expressionList)
        expressionList1=expressionCalcu(expressionList1,operateOrder,0)
        #print(f'operateOrder : {operateOrder[0]}연산')
        expressionList1=expressionCalcu(expressionList1,operateOrder,1)
        #print(f'operateOrder : {operateOrder[1]}연산')
        expressionList1=expressionCalcu(expressionList1,operateOrder,2)
        #print(f'operateOrder : {operateOrder[2]}연산')
        answerList.append(abs(expressionList1[0]))
    print(answerList)
    return max(answerList)


if __name__=="__main__":
    expression="100-200*300-500+20"
    expression2="50*6-3*2"
    solution(expression)