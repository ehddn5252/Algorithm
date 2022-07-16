num = int(input())

paper = [list(map(int, input().split(" "))) for i in range(num)]

# -1, 0 ,1
counter_list = [0, 0, 0]

'''
1. i와 j 시작 위치를 설정해야 하는 데, 이는 나중에 할 것으로 참고하도록 하자.
2. 9 개로 나누는 것을 확인해야 하고, 
'''


def recur(start_i, start_j, limit):
    if limit == 1:
        counter_list[paper[start_i][start_j] + 1] += 1
        return
    braek_flag = False
    start = paper[start_i][start_j]
    for i in range(limit):
        for j in range(limit):
            if start != paper[start_i + i][start_j + j]:
                for ii in range(3):
                    for jj in range(3):
                        recur(start_i + ii * limit, start_j + jj * limit, limit // 3)
                        break_flag = True
                        break
                    if break_flag:
                        break
    counter_list[paper[start_i][start_j] + 1]+=1

recur(0,0,num)
print(counter_list)