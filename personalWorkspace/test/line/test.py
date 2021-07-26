# 조건2
# 대문자 : 65 ~ 90
# 소문자 : 97~122
# 0~9 : 48~57
# ~!@#$%^&* : 126, 33, 64, 35, 36, 37, 94, 38, 42

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

print(satisfied_name_condition("1234567890",48,57))

print(satisfied_dual_name_condition("Bye321",65,90,97,122))