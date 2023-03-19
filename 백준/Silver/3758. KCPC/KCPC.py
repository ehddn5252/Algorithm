"""
1. 최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높다.
2. 최종 점수도 같고 제출 횟수도 같은 경우, 마지막 제출 시간이 더 빠른 팀의 순위가 높다.

1. TestCase 수

"""

testcase = int(input())

for _ in range(testcase):
    n, k, t, m = map(int, input().split(" "))  # 팀의 개수, 문제의 개수, 팀 ID, 로그 엔트리 수
    teams = [[[0 for _ in range(k + 1)], 0, 0, i] for i in range(n + 1)]  # 팀별 [문제별 점수, 제출 횟수]
    now = 0
    for _ in range(m):
        i, j, s = map(int, input().split(" "))  # 각 팀의 ID i, 문제 번호 j, 획득한 점수 s
        if teams[i][0][j] < s:
            teams[i][0][j] = s
        teams[i][1] += 1
        teams[i][2] = now
        now += 1

    teams.sort(key=lambda x: [-sum(x[0]), x[1], x[2]])
    for i in range(len(teams)):
        if t == teams[i][3]:
            print(i + 1)
            break
