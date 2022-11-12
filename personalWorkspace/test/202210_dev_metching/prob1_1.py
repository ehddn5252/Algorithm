import re


def solution(registered_list, new_id):
    d = [0 for _ in range(1000000)]
    d[0]=1
    s = re.sub(r'[0-9]', '', new_id)
    num = re.sub(r'[^0-9]', '', new_id)
    if num!="":
        for i in range(int(num)):
            d[i]=1

    for word in registered_list:
        sub_str = re.sub(r'[0-9]', '', word)

        if sub_str == s:
            sub_num = re.sub(r'[^0-9]', '', word)
            if sub_num!='':
                d[int(sub_num)]=1
    # 등록 리스트에 없다면 바로 등록
    if new_id not in registered_list:
        return new_id
    else:
        for i,n in enumerate(d):
            if n==0:
                return s+str(i)




registered_list = ["cow","cow1","cow2"]
new_id = "cow"
print(solution(registered_list, new_id))