'''
1. 속한 노래가 많이 재생된 장르를 먼저 수록
2. 장르 내에서 많이 재생된 노래를 먼저 수록
3. 장르 내에서 재생 횟수가 같은 노래 중 고유 번호가 낮은 노래를 먼저 수록

'''

def solution(genres, plays):
    
    genre_dict = {}
    sum_dict = {}
    
    for i,(genre, play) in enumerate(zip(genres,plays)):
        
        if genre in genre_dict.keys():
            sum_dict[genre]+=play
            genre_dict[genre].append([i,play])
        else:
            sum_dict[genre]=play
            genre_dict[genre]=[[i,play]]
            
    for i,v in genre_dict.items():
        v.sort(key = lambda x:-x[1])
        genre_dict[i]=v
        
    d2 = sorted(sum_dict.items(),key = lambda x:-x[1] )
    
    answer= []
    for d in d2:
        for i,v in enumerate(genre_dict[d[0]]):
            if i<=1:
                answer.append(v[0])
            
    return answer