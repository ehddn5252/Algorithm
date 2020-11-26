# 작성일 : 20201122
# 작성자 : 김동우
# 문제명 : 수 찾기
# 문제 요약 :
# 0. 배열1,2가 주어진다. 배열 1에 배열 2에 있는 수가 있는 지 확인하고 있으면 1 없으면 0을 출력

# 문제 해설 : 
# 방법 1 
# 0. 해시를 사용한다.
# 시간 복잡도 : O(N)


N=0
inputedList1=[]
M=0
inputedList2=[]
# local함수에서 초기화를 하면 전역 변수라도 적용이 안된다.
def solution():
    int(input())
    inputedList1=list(map(int,input().split()))
    int(input())
    inputedList2=list(map(int,input().split()))
    
    checkDic={}
    for num in inputedList1:
        checkDic[num]=1

    ansList=[]
    for num in inputedList2:
        if not checkDic.get(num):
            ansList.append(0)
        else:
            ansList.append(1)

    for i in ansList:
        print(i)

if __name__ == "__main__":
    solution()