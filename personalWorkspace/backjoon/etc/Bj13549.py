subin, brother = map(int, input().split(" "))
def sol():
    nl = [[subin, 0]]
    visit = [99999 for _ in range(100006)]
    ans_list = [100]
    is_visit = True
    while is_visit:
        is_visit = False
        l = nl
        nl = []
        while l:
            popped = l.pop()
            if popped[0]==brother:
                ans_list.append(popped[1])
            while popped[0]*2 <= 100005 and visit[popped[0]*2]>popped[1]:
                is_visit = True
                nl.append([popped[0]*2, popped[1]])
                visit[popped[0] * 2] = popped[1]
                popped[0]*=2

            if popped[0]-1>=0 and visit[popped[0]-1]>popped[1]+1:
                is_visit=True
                nl.append([popped[0]-1,popped[1]+1])
                visit[popped[0] - 1] = popped[1]+1

            if popped[0]+1<=100005 and visit[popped[0]+1]>popped[1]+1:
                is_visit = True
                nl.append([popped[0]+1, popped[1]+1])
                visit[popped[0] + 1] = popped[1]+1

    print(min(ans_list))

if subin == brother:
    print(0)
else:
    sol()
