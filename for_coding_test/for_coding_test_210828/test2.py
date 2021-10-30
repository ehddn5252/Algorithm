
'''
풀이 방법
1. 장르별로 정렬하고, 인덱스를 저장한다. 재생 횟수대로 정렬한다. 
2. 장르 순서대로니까 장르를 순서대로 모두 저장해야 한다.
'''
    


def solution(genres, plays):
    answer: list = []
    dic: dict = {}
    PLAY: int = 0
    INDEX: int = 1
        
    for genre in genres:
        dic[genre]=[]
        
    for i,(genre,play) in enumerate(zip(genres,plays)):
        dic[genre].append([play,i])

    max_play: list= ["",float("-inf"),-1]
    
    while(dic):
        for g_index,genre in enumerate(genres):
            for i in range(len(dic[genre])):
                if dic[genre][i][1] > max_play[1]:
                    max_play = [genre,dic[genre][i][PLAY],dic[genre][i][INDEX]]
        dic[max_play[0]].sort(key= lambda x:(-x[1],x[2]))
                 
        for (play,index) in dic[max_play[0]]:
            answer.append([index])
                 
        while max_play[0] in genres:
            genres.remove(max_play[0])
                 
        del dic[max_play[0]]
                 
    for key,value in dic.items():
        print(f"key : {key}, value : {value}")
    return answer

if __name__=="__main__":
    genres = ["classic","pop","classic","classic","pop"]
    plays = [500,600,150,800,2500]
    print(solution(genres,plays))