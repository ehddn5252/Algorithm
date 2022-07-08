r, c, k = map(int, input().split(" "))
r -= 1
c -= 1
A = [list(map(int, input().split(" "))) for _ in range(3)]
new_A = [[] for _ in range(3)]

num_dict: dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}


# 행의 개수가 열의 개수보다 크거나 같을 때 정렬한다.

def dict_reset():
    global num_dict
    num_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}


def counting(l):
    for i in l:
        num_dict[i] += 1


def sort_row():
    global new_A, A
    new_A = [[] for i in range(len(A))]
    max_count = 0
    for i in range(len(A)):
        count = 0
        for j in A[i]:
            num_dict[j] += 1

        num_l = list(num_dict.items())
        num_l.sort(key=lambda x: (x[1], x[0]))

        if len(num_l) > 50:
            l = 50
        else:
            l = len(num_l)
        for j in range(l):
            k, v = num_l[j]
            count += 1
            new_A[i].append(k)
            new_A[i].append(v)

        if max_count < count:
            max_count = count
        dict_reset()


    max_count *= 2
    for i in range(len(A)):
        if len(new_A[i]) < max_count:
            for j in range(max_count - len(new_A[i])):
                new_A[i].append(0)

    A = new_A



def sort_col():
    global new_A, A
    new_A = [[] for i in range(len(A[0]))]
    max_count = 0
    for i in range(len(A[0])):
        count = 0

        for k in range(len(A)):
            num_dict[A[k][i]] += 1
        num_l = list(num_dict.items())
        num_l.sort(key=lambda x:(x[1],x[0]))

        if len(num_l)>50:
            l = 50
        else:
            l = len(num_l)
        for j in range(l):
            k, v = num_l[j]
            count += 1
            new_A[i].append(k)
            new_A[i].append(v)

        if max_count < count:
            max_count = count
        dict_reset()

    max_count *= 2
    for i in range(len(new_A)):
        if len(new_A[i]) < max_count:
            for j in range(max_count - len(new_A[i])):
                new_A[i].append(0)

    A = [[] for _ in range(len(new_A[0]))]
    for i in range(len(new_A[0])):
        for j in range(len(new_A)):
            A[i].append(new_A[j][i])


time = 0

while len(A) <= 100 and len(A[0]) <= 100:
    print(A)
    if A[r][c] == k:
        print(time)
        break
    # 행의 개수 >= 열의 개수
    if len(A) >= len(A[0]):
        sort_row()
    else:
        sort_col()

    time += 1

else:
    print(-1)
