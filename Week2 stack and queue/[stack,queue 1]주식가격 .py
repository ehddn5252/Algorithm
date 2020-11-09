# 작성 날짜 : 20201109
# 작성자 : 김동우
# 문제 명 : 주식 가격
# 문제 유형: stack, queue ( 위 유형을 사용하지 않고 2중 for문돌려서 풀었다)
# 문제 요약 : 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인가? 

# 풀이 1 
# 2중 for문을 사용해서 처음부터 하나씩 비교했다.
# 시간 복잡도 :  O(N^(3/2)) 
# 풀이 2 
# stack 사용하면 시간복잡도가 O(N)이 나올 것이다.

def solution1(prices):
    answer = []
    for object1 in range(0,len(prices)-1):
        time=0
        for compare in range(object1+1,len(prices)):
            time+=1
            if prices[object1]>prices[compare]:
                break
        answer.append(time)
    answer.append(0)
    return answer

# 파이썬에서 stack을 사용할 때 리스트에 list.append(a)로 넣고 list.pop()으로 뺀다.



