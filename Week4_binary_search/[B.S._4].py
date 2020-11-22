# 작성일 : 20201119,20
# 작성자 : 김동우
# 문제명 : 가장 긴 증가하는 부분 수열2
# 문제 요약 :
# 1. 수열 A가 주어진다.
# 2. 가장 긴 증가하는 부분 수열을 구하는 프로그램 작성
# ex1) A={50,10,30,20,40} 이면 3 ({10,30,40}) 이 답이 된다.
# ex2) A={30,40,50,20,40,60} 이면 4({30,40,50,60}) 이 답이 된다.

# 문제 해석 :
# 1. 우측의 가장 큰 수를 찾는다.
# 2. 좌측의 가장 작은 수를 찾는다.
# 3. 가장 작은 수를 stack에 추가한다.
# 4. stack의 top과 가장 작은수의 오른쪽 값부터 비교해서 우측 값이 더 크면 stack에 추가한다.
# 5. 만약 우측 값이 더 작으면 pop하고 

def input_Func():
    int(input())
    inputedList=[]
    inputedList=list(map(int,input().split()))
    return inputedList


def solution(inputedList):
    max=[0,0]
    min=[999999,0]
    # 좌측 
    for index,num in enumerate(inputedList):
        if num>=max[0]:
            max=[num,index]
        if num<min[0]:
            min=[num,index]
    ans=1
    queue=[]
    for i,num in enumerate(inputedList):
        if i>max[1]:
            break
        elif min[0]<num:
            ans=ans+1

            min[0]=num
            min[1]=i
    print(ans)




if __name__ == "__main__":
    solution(input_Func())