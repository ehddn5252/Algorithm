import re

def solution(registered_list, new_id):
    # 등록 리스트에 없다면 바로 등록
    if new_id not in registered_list:
        return new_id
    else:
        # s = re.match('[a-z]*',new_id)
        s = re.sub(r'[0-9]', '', new_id)
        num = re.sub(r'[^0-9]', '', new_id)
        if num == "":
            num = "1"
        t = s + str(num)
        while t in registered_list:
            num = int(num) + 1
            t = s + str(num)

        return t


registered_list = ["cow","cow1","cow2"]
new_id = "cow"
solution(registered_list, new_id)