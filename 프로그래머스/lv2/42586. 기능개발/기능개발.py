def solution(progresses, speeds):
    answer = []
    start_index = 0
    
    while True:
        if start_index==len(progresses):
            break
        count=0
        for i,speed in enumerate(speeds):
            progresses[i]+=speed
        
        while start_index<len(progresses):
            if progresses[start_index]>=100:
                count+=1
                start_index+=1
            else:
                break
                
        if count!=0:
            answer.append(count)
                
    return answer