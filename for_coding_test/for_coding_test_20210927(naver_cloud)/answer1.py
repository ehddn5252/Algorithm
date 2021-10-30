import copy

entire_hash = {}
ALPHABETS = ["A","B","C","E","K","L","M","Q","T","X","Y"]
for alphabet in ALPHABETS:
    entire_hash[alphabet] = 0

empty_hash = copy.deepcopy(entire_hash)
empty_char = "."

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(rows, cols, maps):
    global mini_hash
    if cols <=-1 or cols>=max_col or rows <=-1 or rows>= max_row:
        return

    if maps[rows][cols]==empty_char:
        return

    if check_list[rows][cols]:
        return
    else:
        check_list[rows][cols] = True
        key = maps[rows][cols]
        mini_hash[key]+=1

    for i in range(4):
        DFS(rows+dx[i],cols+dy[i],maps)

def make_result_hash():
    after_hash = copy.deepcopy(empty_hash)
    max_value = 0
    max_alphabet = ""
    for key,value in mini_hash.items():
        if value>=max_value:
            max_alphabet = key
            max_value = value
    after_hash[max_alphabet] += max_value
    #print("mini_hash")
    #print(mini_hash)
    for key,value in mini_hash.items():
        if value < max_value:
            after_hash[max_alphabet] = after_hash[max_alphabet] + value
        elif key!=max_alphabet and value == max_value:
            after_hash[key] += value

    return after_hash

def solution(maps):
    global check_list
    global max_row
    global max_col
    max_row = len(maps)
    max_col = len(maps[0])
    check_list = [[False for _ in range(max_col)] for _ in range(max_row)]

    for rows in range(len(maps)):
        for cols in range(len(maps[0])):
            if maps[rows][cols]==empty_char:
                check_list[rows][cols]=True


    for rows in range(len(maps)):
        for cols in range(len(maps[0])):
            global mini_hash
            mini_hash = copy.deepcopy(empty_hash)
            if check_list[rows][cols]==False:
                DFS(rows=rows, cols=cols, maps=maps)
                after_hash = make_result_hash()
                for key,value in after_hash.items():
                    entire_hash[key]+=value
    return max(entire_hash.values())
