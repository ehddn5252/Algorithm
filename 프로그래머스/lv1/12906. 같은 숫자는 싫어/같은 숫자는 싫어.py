from collections import deque

def solution(arr):
    # s = deque([arr[0]])
    s = [arr[0]]
    for i,v in enumerate(arr):
        if i==0:
            continue
            
        if s[-1]!=v:
            s.append(v)
    return s
    print(s)
            