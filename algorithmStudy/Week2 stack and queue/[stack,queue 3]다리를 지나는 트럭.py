# 작성일 : 20201109
# 작성자 : 김동우
# 문제 유형 : stack queue
# 문제 요약 : 트럭들이 다리를 지나야 한다. 다리는 최대로 버틸 수 있는 무게가 있고 그 무게를 초과하지 않게 트럭을 계속
# 다리로 진입시킬때 걸리는 시간을 구하라.
# 문제 풀이 :
# 1. queue에 다리 길이만큼 0으로 초기화한다. 반복마다 계속 시간이 흐르게 구현한다 time +=1
# 2. 시작할때 다리 위 트럭이 나가는 것을 먼저 생각한다(truck_weights_sum-=queue.pop())
# 3. 진입+ 다리위의 트럭 무게 합보다 다리가 버틸 수 있는 무게가 더 크면 트럭 무게를 다리에 넣고 아니면 0을 넣는다
# 4. truck_weights[-1]까지 하다보면 마지막 트럭이 진입하고, 그 시점으로부터 다리 길이를 더하면 답이 나온다.
# 시간 복잡도 O(N)

def solution(bridge_length, weight, truck_weights):
    time = 0
    queue=[]
    index=0
    for _ in range(bridge_length):
        queue.append(0)
    truck_weights_sum=0
    while index<len(truck_weights):
        time+=1
        truck_weights_sum-=queue.pop()
        if weight>=truck_weights_sum+truck_weights[index]:
            queue.insert(0,truck_weights[index])
            truck_weights_sum+=truck_weights[index]
            index+=1
        else:
            queue.insert(0,0)
    time+=bridge_length
    return time