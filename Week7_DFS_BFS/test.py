# 작성일 : 20210105
# 작성자 : 김동우
# 문제명 : 타겟 넘버
# 문제 요약 : 0이아닌 N개의 정수가 있다. 이 수를 적절히 더하거나 빼서 
# 타겟 넘버를 만들어라.

# 문제 풀이 : 
# 1. 완전탐색 사용한다. 모든 경우의 수 다 확인해도 시간초과 안걸리면 성공이다.
# 2. 모든 경우의 수를 확인하는 방법
# 3. permutationList를 만든다.
# 4. permutationList의 인자가 0이면 + 1이면 -하고 다음으로
# 5. 끝까지가서 값을 비교

i=0
def print_order_array(order):
    global i
    i+=1
    print(i)
    print(order)

answer=0
def permutation(order,k,n,target,sumValue):
    global answer
    if k==n:
        print_order_array(order)
        if sumValue==target:
            answer+=1
    else:
        check = [False]*n
        for i in range(k):
            check[order[i]]=True

        for i in range(n):
            if check[i]==False:
                sumValue+=numbers[i]
                order[k]=i
                permutation(order,k+1,n,target,sumValue)
            else:
                sumValue-=numbers[i]

def soluton(numbers,target):
    order=[]
    for _ in range(len(numbers)):
        order.append(0)
    permutation(order,0,len(order),target,0)


if __name__ == "__main__":
    numbers=[1,1,1,1,1]
    target=3
    soluton(numbers,target)
    print(answer)
    