def solution(participant, completion):
    dict = {}
    for i in participant:
        if i in dict.keys():
            dict[i]+=1
        else:
            dict[i]=1
    for i in completion:
        if i in dict.keys():
            dict[i]-=1
    
    for key,value in dict.items():
        if value!=0:
            return key
