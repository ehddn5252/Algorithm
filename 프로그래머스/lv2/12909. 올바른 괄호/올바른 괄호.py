def solution(s):
    stack = [s[0]]
    for i,v in enumerate(s):
        if i==0:
            continue
            
        if v=="(":
            stack.append(v)    
        elif (len(stack)==0 and v==")") or (stack[-1]==")" and v==")"):
            return False

        elif stack[-1]=="(" and v==")":
            stack.pop()
    
    if (len(stack)==0):
        return True
    else:
        return False