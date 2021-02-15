# 작성일자 : 20210214
# 문제명 : 징검다리 [프로그래머스 이분탐색]
# 문제 요약 :
# 1. 출발지점으로부터 distance만큼 떨어진 곳에 도착지점이 있다.
# 2. 그 사이에 바위들이 놓여있고, 바위 중 몇개를 제거하려 한다.
# 3. 출발지점, 도착지점, 바위 간의 거리의 최솟값이 가장 큰 경우로 바위를 제거할때 최솟 값을 return하라

# 문제 풀이 : 시작점과 끝 점을 예외 처리 해야한다.
# 1. 바위들을 모두 sort하고 distance를 list에 더한다.
# 2. 최솟값을 start로 설정하고 end=max로 설정한다.
# 3. mid= (start+end)//2 로 두고 이것이 두 바위사이 거리의 임곗값으로 둔다. 
# 4. for문을 돌아 모든 rock사이 각각의 거리를 비교한다
# 5. 만약 이 임곗값보다 두 바위 사이의 거리가 작다면 그 바위를 cut한다.
# 6. 만약 이 임곗값보다 두 바위 사이의 거리가 크거나 같다면 통과한다.
# 7. for을 다 돌고 제거된 rock의 수를 확인한다.
# 7-1. 제거된 rock의 수가 n보다 크다면 임곗값을 낮춘다 더 많이 제거하는 경우는 정답이 될 수 없다. end=mid-1
# 7-2. 제거된 rock의 수가 n보다 작다면 임곗값을 높이고 정답을 저장한다. start=mid+1 answer=mid


def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    start=0
    end=distance
    
    while start<=end:
        mid=(start+end)//2
        removedRockNum=0
        prevRock=0
        for rock in rocks:
            if rock-prevRock<mid:
                removedRockNum+=1
            else:
                prevRock=rock
        if removedRockNum>n:
            end=mid-1
        elif removedRockNum<=n:
            answer=mid
            start=mid+1
    print(answer)
    return answer

if __name__=="__main__":
    distance=25
    rocks=[2, 14, 11, 21, 17]
    n=2
    solution(distance, rocks, n)
