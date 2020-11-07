
genres =  ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
def solution(genres, plays):
    answer = []
    ansDic={}
    for num,i in enumerate(genres):
       ansDic[i]=[]

    for num,i in enumerate(genres):
        ansDic[i].append(plays[num])
        ansDic[i].append(num)

    ansDic.sort
    for i in range(genres):
        
    return answer