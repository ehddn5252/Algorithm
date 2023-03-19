def switch(input_value):
    return 1 - input_value


N = int(input())

init_state = list(map(int, input()))
final_state = list(map(int, input()))
INF = 2147000000


def switching(input_state, final_state):
    global N
    state = input_state[:]
    ans = 0
    for i in range(1, N):
        if state[i - 1] != final_state[i - 1]:
            ans += 1
            for j in range(i - 1, i + 2):
                if j < N:
                    state[j] = switch(state[j])
    return ans if state == final_state else INF


ans = switching(init_state, final_state)

init_state[0] = switch(init_state[0])
init_state[1] = switch(init_state[1])

ans = min(switching(init_state, final_state) + 1, ans)
if ans == INF:
    ans = -1
print(ans)
