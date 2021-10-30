import copy

entire_hash = {}
ALPHABETS = ["A","B","C","E","K","L","M","Q","T","X","Y"]
for alphabet in ALPHABETS:
    entire_hash[alphabet] = 0

empty_hash = copy.deepcopy(entire_hash)
empty_char="."

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def DFS(rows,cols,maps):
    global mini_hash
    if cols <=-1 or cols>=max_col or rows <=-1 or rows>=max_row:
        return 

    if maps[rows][cols]==empty_char:
        return

    if check_list[rows][cols]:
        return
    else:
        check_list[rows][cols]=True
        key=maps[rows][cols]
        mini_hash[key]+=1

    for i in range(4):
        DFS(rows+dx[i],cols+dy[i],maps)
        
def make_result_hash():
    after_hash =copy.deepcopy(empty_hash)
    max_value = 0
    max_alphabet = ""
    for key,value in mini_hash.items():
        if value>=max_value:
            max_alphabet = key
            max_value = value
    after_hash[max_alphabet] += max_value
    print("mini_hash")
    print(mini_hash)
    for key,value in mini_hash.items():
        if value < max_value:
            after_hash[max_alphabet] = after_hash[max_alphabet]+ value
            print("-----")
            print(after_hash[max_alphabet])
        elif key!=max_alphabet and value == max_value:
            after_hash[key] += value

    print(after_hash)
    return after_hash


def solution(maps):
    global check_list
    global max_row
    global max_col
    max_row = len(maps)
    max_col = len(maps[0])
    check_list = [[False for j in range(max_col)] for i in range(max_row)]
    print(check_list)

    for rows in range(len(maps)):
        for cols in range(len(maps[0])):
            if maps[rows][cols]==empty_char:
                check_list[rows][cols]=True

    for rows in range(len(maps)):
        for cols in range(len(maps[0])):
            global mini_hash
            mini_hash=copy.deepcopy(empty_hash)
            if check_list[rows][cols]==False:
                print("-----")
                DFS(rows = rows,cols = cols, maps = maps)
                after_hash = make_result_hash()
                print("after")
                print(after_hash)
                for key,value in after_hash.items():
                    entire_hash[key]+=value
                print("entire_hash")
                print(entire_hash)
    print(max(entire_hash.values()))
    return max(entire_hash)

if __name__=="__main__":
    maps1 = ["XY..","YX..","..YX",".AXY"]
    solution(maps1)



'''
풀이 방법:
전형적인 BFS방법이다.
0. boolean check_list를 하나 만든다.
1. 전체 hash와 영토별 모든 알파벳 hash, 전투 후 hash를 만든다. 영토를 쭉 돌면서 \
    hash에 알파벳 개수를 추가한다.
2. hash에서 알파벳 개수가 가장 많은 것을 찾고 만약 수가 같은 게 있다면 \
    알파벳 순서가 뒤인 것이 흡수하는 map을 만든다.
3. map에서는 BFS로 전체를 돌려본다.
'''

# rows cols의 인덱스를 DFS로 넘기고, 그것의 check_list를 확인해서 방문한 곳이면 pass
# 방문한 곳이 아니면 알파벳을 확인해서 hash에 알파벳 수를 더한다.