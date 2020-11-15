# 작성자 : 김동우
# 작성일자 : 20201115
#
# 문제 요약 : 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 리스트로 만들어 정렬했을 때, k번째에 있는 수를 구하기

# 주의사항 : index계산할 때 0부터 시작하는 것에 주의한다.
array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    slicedList=[]
    # comands의 수만큼 반복해서 answer에 append해야한다.
    times=len(commands)
    for orderIndex in range(times):
        # commands의 [orderIndex][0]에는 어디서부터 시작할 지, commands[orderIndex[1]에는 어디까지인지
        # 저장되어 있어서 그 구간을 slicedList에 저장한다. 
        for i in range(commands[orderIndex][0]-1,commands[orderIndex][1],1):
            slicedList.append(array[i])
        # slicedList 정렬하고 k번째에 있는 수를 답에 추가한다.
        slicedList.sort()
        
        answer.append(slicedList[commands[orderIndex][2]-1])
        # 다 사용했으면 slicedList를 비워준다.
        slicedList=[]
    print(answer)
    return answer
    
if __name__ == "__main__":
    solution(array,commands)