# 어떤 메신저 회사에서는 신규 아이디의 password가 다음 규칙을 만족하도록 강제하고 있다.
# 4종류의 문자 그룹을 제외한 다른 어떤 문자도  포함해서는 안된다.

def solution(inp_str):
    answer=[]
    # 조건 1
    if len(inp_str)<=7 or len(inp_str)>15:
        answer.append(1)

    # 조건2
    # 대문자 : 65 ~ 90
    # 소문자 : 97~122
    # 0~9 : 48~57
    # ~!@#$%^&* : 126, 33, 64, 35, 36, 37, 94, 38, 42

    condition2_check_list=[False,False,False,False]
    condition3_check_list=[0,0,0,0]
    for inp_char in inp_str:
        if 65<=ord(inp_char) and ord(inp_char)<=90:
            condition2_check_list[0]=True
            condition3_check_list[0]=1
        elif 97<=ord(inp_char) and ord(inp_char)<=122:
            condition2_check_list[1]=True
            condition3_check_list[1]=1
        elif 48<=ord(inp_char) and ord(inp_char)<=57:
            condition2_check_list[2]=True
            condition3_check_list[2]=1
        elif ord(inp_char)== 126 or ord(inp_char)== 33 or ord(inp_char)==64 or ord(inp_char)== 35 or ord(inp_char)== 36 or ord(inp_char)== 37 or ord(inp_char)== 94 or ord(inp_char)==38 or ord(inp_char)== 42:
            condition2_check_list[3]=True
            condition3_check_list[3]=1
        
        if True not in condition2_check_list:
            answer.append(2)
        condition2_check_list=[False,False,False,False]
    
    # 조건 3
    if sum(condition3_check_list)<3:
        answer.append(3)

    # 조건4
    beforIndex=0
    stack=1
    for index,value in enumerate(inp_str):
        if index==0: continue
        if inp_str[index]==inp_str[beforIndex]:
            stack+=1
        else:
            stack=1
        if stack>=4:
            answer.append(4)
            break
        beforIndex=index
    
    # 조건 5
    inp_str_hash={}
    for inp_char in inp_str:
        if not inp_char in inp_str_hash:
            inp_str_hash[inp_char]=1
        else:
            inp_str_hash[inp_char]+=1
    
    for _,value in inp_str_hash.items():
        if value>=5:
            answer.append(5)

    # 모두 만족할때
    if not answer:
        return [0]
    answer.sort()
    answer=list(set(answer))
    
    return answer