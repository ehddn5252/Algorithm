# 작성자 : 김동우
# 작성일자 : 20201115
#
# 문제 요약 : 0 또는 양의 정수의 list가 주어졌을 때 정수를 이어 붙여 만들 수 있는 가장 큰 수를 구하라
# 해결 방법 1 

numbers=[6, 10, 2]

def solution(numbers):
    numbersStr=[]

    for i in numbers:
        numbersStr.append(str(i))
        sortedNumberStr=[]
    sortedNumberStr=sorted(numbersStr,reverse=True)
    tmp=""
    for pivotIndex in range(len(sortedNumberStr)):
        for j in range(pivotIndex+1,len(sortedNumberStr)):
            if len(sortedNumberStr[j])==len(sortedNumberStr[pivotIndex]):
                break
            if sortedNumberStr[pivotIndex]+sortedNumberStr[j]<sortedNumberStr[j]+sortedNumberStr[pivotIndex]:
                tmp=sortedNumberStr[pivotIndex]
                sortedNumberStr[pivotIndex]=sortedNumberStr[j]
                sortedNumberStr[j]=tmp

    return ''.join(sortedNumberStr)
    

if __name__ == "__main__":
    print(solution(numbers))