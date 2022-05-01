import sys
'''
1. 노드는 한 줄로만 이어져 있다 그래서 계속 쭉 타고 들어가면 된다.
2. 그것을 dp에 모아놓자
'''

def find_parent(num)->list:
    global init_l
    for i,v in enumerate(_map[num]):
        init_l.append(v)
        find_parent(v)


N = int(sys.stdin.readline())
_map = [[]for i in range(N)]
dp = [[] for i in range(N)]

for i in range(N-1):
    start, end = map(int, sys.stdin.readline().split(" "))
    if(start>end):
        tmp=start
        start=end
        end=tmp
    _map[end-1].append(start-1)

for i in range(N):
    init_l=[i]
    find_parent(i)
    dp[i] = sorted(init_l, reverse=True)

N2 = int(sys.stdin.readline())
for i in range(N2):
    num1, num2 = map(int, sys.stdin.readline().split(" "))
    num1 -= 1
    num2 -= 1
    break_flag=False
    for i in range(0,len(dp[num1])):
        for j in range(len(dp[num2])):
            if(dp[num1][i]==dp[num2][j]):
                print(dp[num1][i]+1)
                break_flag=True
            if(break_flag): break
        if (break_flag): break