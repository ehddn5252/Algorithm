rule1_str = ['a', 'e', 'i', 'o', 'u']

def check_rule1(str1):
    global rule1_str
    for i in range(len(str1)):
        if str1[i] in rule1_str:
            return True
    return False


def check_rule2(str1):
    global rule1_str
    vowel_check = 0  # 1 은 모음 2는 자음
    tmp_stack = 0
    for i in range(len(str1)):
        # 모음인 경우
        if str1[i] in rule1_str:
            # 이전도 모음이면 모음 스택 추가
            if vowel_check == 1:
                tmp_stack += 1
            else:
                vowel_check = 1
                tmp_stack = 1
        # 자음이면 자음 스택 추가
        elif 97 <= ord(str1[i]) <= 122:
            if vowel_check == 2:
                tmp_stack += 1
            else:
                vowel_check = 2
                tmp_stack = 1
        else:
            tmp_stack = 0
            vowel_check = 0
        if tmp_stack >= 3:
            return False
    return True


def check_rule3(str1):
    tmp = '-21474836475151234'
    tmp_stack = 1
    for i in range(len(str1)):
        # 같은 글자가 아니면 stack을 1로
        if str1[i] != tmp:
            tmp = str1[i]
            tmp_stack = 1
        else:
            # 같은 글자면 stack이 올라감
            tmp_stack += 1
        # 스택이 2면 체크한다.
        if tmp_stack == 2:
            if str1[i] == 'e' or str1[i] == 'o':
                continue
            return False
    return True


while True:
    st = input()
    if st == 'end':
        break

    if check_rule1(st) and check_rule2(st) and check_rule3(st):
        print(f"<{st}> is acceptable.")
    else:
        print(f"<{st}> is not acceptable.")