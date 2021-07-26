# 조건2
# 대문자 : 65 ~ 90
# 소문자 : 97~122
# 0~9 : 48~57
# ~!@#$%^&* : 126, 33, 64, 35, 36, 37, 94, 38, 42

def satisfied_name_length(name,min_value,max_value):
    if len(name)<min_value or len(name)>max_value:
        return False
    else:
        return True

def satisfied_name_condition(name,min_value,max_value):
    ret = True
    for char in name:
        if min_value<=ord(char) and ord(char)<=max_value:
            continue
        else:
            return False
    return ret


def satisfied_dual_name_condition(name,min_value1,max_value1,min_value2,max_value2):
    ret = True
    for char in name:
        if min_value1<=ord(char) and ord(char)<=max_value1 or min_value2<=ord(char) and ord(char)<=max_value2:
            continue
        else:
            return False
    return ret



def confirm_flag_arg(flag_type,is_flag):
    if flag_type=="NULL":
        return 0,1
    elif flag_type=="NUMBER":
        return 1,2
    elif flag_type=="STRING":
        return 2,2
    # added
    elif flag_type=="NUMBERS":
        return 3,3
    # added
    elif flag_type=="STRINGS":
        return 4,4
    else:
        return -1,2

def check_argment(flag_type,argument):
    # NUMBER
    if flag_type==1:
        return satisfied_name_condition(argument,48,57),1
    # STRING
    elif flag_type==2:
        return satisfied_dual_name_condition(argument,65,90,97,122),1
    # added
    # NUMBERS
    elif flag_type==3:
        return satisfied_name_condition(argument,48,57),3
    # STRINGS
    # added
    elif flag_type==4:
        return satisfied_dual_name_condition(argument,65,90,97,122),4

        

def solution(program, flag_rules, commands):
    answer = []

    # hash에 flag정보를 넣는다.
    flag_hash={}
    for flag_rule in flag_rules:
        flag_name,flag_type_name=flag_rule.split()
        flag_hash[flag_name]=flag_type_name
    print(flag_hash)
    
    flag_type=0
    for command in commands:
        command_list=list(command.split())

        # program check
        if command_list[0]!=program:
            answer.append(False)
            continue
        
        # is_flag가 True일 때  flag가 오는 자리 False이면 argment가 오는 자리
        is_flag=1
        is_break=False
        check_argment_value=True
        for _,code in enumerate(command_list[1:]):
            if is_flag==3 or is_flag==4:
                inp_flag_type=flag_hash.get(code,0)
                if inp_flag_type==0:
                    if is_flag==3:
                        check_argment_value,is_flag=check_argment(3,code)
                    else:
                        check_argment_value,is_flag=check_argment(4,code)
                    if check_argment_value==False:
                        answer.append(False)
                        is_break=True
                        break
                else:
                    is_flag=1

            if is_flag==1:
                inp_flag_type=flag_hash.get(code,0)
                flag_type,is_flag=confirm_flag_arg(inp_flag_type,is_flag)
                if flag_type==-1:
                    answer.append(False)
                    is_break=True
                    break
            #argument 처리
            elif is_flag==2:
                is_flag=1
                check_argment_value,is_flag=check_argment(flag_type,code)
                if check_argment_value==False:
                    answer.append(False)
                    is_break=True
                    break
        if is_break==False:
            answer.append(True)
        else:
            is_break=False

    return answer