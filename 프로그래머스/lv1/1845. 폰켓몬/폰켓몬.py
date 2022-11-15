def solution(nums):
    answer = 0
    size = len(nums)/2
    dict = {}
    
    for num in nums:
        if num in dict.keys():
            dict[num]+=1
        else:
            dict[num]=1
    
    if len(dict)>size:
        return size
    else:
        return len(dict)
