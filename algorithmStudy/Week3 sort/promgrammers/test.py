# 작성자 : 김동우
# 작성일자 : 20201115
#
# 문제 요약 : 0 또는 양의 정수의 list가 주어졌을 때 정수를 이어 붙여 만들 수 있는 가장 큰 수를 구하라
# 해결 방법 1 
# 1. 첫번째자리 비교 
# 2. 두번째자리 비교
# 3. 세번째자리 비교 
# 4. 네번째자리 비교
# 해결 방법 2
# 1. 받아오는 숫자를 문자열로 list에 저장한다.
# 2. list.sort(reverse=True) 로 역순으로 정렬한다
# 3. 위 방법은 크기가 다른 경우 문자열의 크기가 큰 것을 앞에 둔다. 
# 4. 문자열의 크기가 작은 것을 앞에 두는 방법으로 sort하는 방법을 찾아야한다.

# 1회 sol을 목표로하자.
numbers= [6, 10, 2,4,50,5]


def solution(numbers):
    stringList=[]
    for i in numbers:
        stringList.append(str(i))

    stringList1=(sorted(stringList,reverse=True))
    #print(stringList1)
    for pivotIndex,pivot in enumerate(stringList1):
        for compareIndex in range(pivotIndex+1,len(stringList1)):
            if len(pivot)>len(stringList1[compareIndex]):
                for i in range(len(stringList1[compareIndex])):
                    if pivot[i]==stringList1[compareIndex][i]:
                        continue
                    elif pivot[i]<stringList1[compareIndex][i]:
                        break
                    elif pivot[i]>stringList1[compareIndex][i]:
                        tmp=stringList1[pivotIndex]
                        stringList1[pivotIndex] =stringList1[compareIndex]
                        stringList1[compareIndex]=tmp
                        break

                if(pivot[len(stringList1[compareIndex])]<pivot[0]):
                    tmp=stringList1[pivotIndex]
                    stringList1[pivotIndex] =stringList1[compareIndex]
                    stringList1[compareIndex]=tmp

    #print(stringList1)
    return ''.join(stringList1)


if __name__ == "__main__":
    print(solution(numbers))