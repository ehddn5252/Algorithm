n = int(input())
recommand = int(input())
l = list(map(int, input().split(" ")))
"""
1. map에 시간 순서를 같이 저장 한다.

"""
map1 = {}
for i, rec_num in enumerate(l):

    if rec_num not in map1.keys():
        if len(map1) == n:
            tmp = sorted(map1.items(),key=lambda x:(x[1][0],x[1][1]))
            del map1[tmp[0][0]]
        map1[rec_num] = [1, i]
    else:
        map1[rec_num] = [map1.get(rec_num)[0] + 1, map1.get(rec_num)[1]]

for i in sorted(map1.keys()):
    print(str(i)+" ", end="")
