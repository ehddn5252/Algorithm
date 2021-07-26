# 작성일 : 20210718
# 작성자 : 김동우
# 문제 요약 : 
'''
1. 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1,...xN이고 집 여러개가 같은 좌표를 가지는 일은 없다.
2. 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
3. C 개의 공유기를 N개의 집에 적당히 설치해서 가장 인접한 두 공유기 사이의 거리를 최대로 만드는 프로그램 작성하기

'''

# 문제 해설 : 
'''
1. 가장 인접한 두 공유기 사이의 최대 거리를 max와 min의 산술평균값으로 설정
2. 만약 이 값으로 max-min을 나눴을 때 C보다 작다면 mid값에 (max-mid)//2를 더한다.

3. 만약 이 값으로 max-min을 나눴을 때 C보다 크다면 mid 값에 (mid-min)//2 를 뺀다.

'''

# 입력 처리
N, C  = map(int, input().split())
house_position_list = [] 

for i in range(N):
    position = int(input())
    house_position_list.append(position)

max_value = house_position_list[-1]
min_value = house_position_list[0]
mid = (max_value + min_value)//2
answer = 0
# compare//mid 값은 전체 거리 최대값
compare = max_value - min_value
i=100
# C는 공유기의 개수이다. 공유기 개수보다 크면 안된다.
while(i):
    i-=1
    if compare//mid>C:
        mid=(max_value+mid)//2

    elif compare//mid<C:
        answer=compare//mid
        mid=(mid-min_value)//2
        
    else:
        answer=compare//mid


print(answer)