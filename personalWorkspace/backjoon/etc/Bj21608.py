N = int(input())
input_infos = [list(map(int, input().split(" "))) for _ in range(N ** 2)]
new_sit = [[0 for _ in range(N)] for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
like_number_score_list: list = [0, 1, 10, 100, 1000]
answer = 0
"""
1. 맨 처음 친구는 1.1 위치에 둔다.
2. 좋아하는 학생이 가장 많이 인접한 칸에 둔다.
3. 인접한 칸 중 비어있는 공간이 많은 칸으로 둔다.
4. 행, 열 작은 순서대로 간다.
"""

for input_index, input_info in enumerate(input_infos):
    # row, col, 좋아하는 친구수, 주변 빈공간 수
    best_sit_info = [0, 0, 0, 0]
    # 1. 맨 처음 친구는 1.1 위치에 둔다.
    if input_index == 0:
        new_sit[1][1] = input_info[0]
    else:
        # row 작은 그 다음 col 작은 순서대로 확인
        for row_index in range(N - 1, -1, -1):
            for col_index in range(N - 1, -1, -1):
                empty_num = 0
                like_friend_num = 0
                # 자리가 비어 있으면 확인
                if new_sit[row_index][col_index] == 0:
                    # 그 자리의 동서남북 확인
                    for i in range(4):
                        new_row = row_index + dx[i]
                        new_col = col_index + dy[i]
                        if new_row >= 0 and new_row < N and new_col >= 0 and new_col < N:
                            if new_sit[new_row][new_col] == 0:
                                empty_num += 1
                            elif new_sit[new_row][new_col] in input_info[1:]:
                                like_friend_num += 1
                    if like_friend_num > best_sit_info[2]:
                        best_sit_info = [row_index, col_index, like_friend_num, empty_num]
                    elif like_friend_num == best_sit_info[2]:
                        if empty_num >= best_sit_info[3]:
                            best_sit_info = [row_index, col_index, like_friend_num, empty_num]
        new_sit[best_sit_info[0]][best_sit_info[1]] = input_info[0]

for row_index in range(N):
    for col_index in range(N):
        like_friend_num = 0
        # 자리가 비어 있으면 확인
        for input_info in input_infos:
            if new_sit[row_index][col_index] == input_info[0]:
                # 그 자리의 동서남북 확인
                for i in range(4):
                    new_row = row_index + dx[i]
                    new_col = col_index + dy[i]
                    if new_row >= 0 and new_row < N and new_col >= 0 and new_col < N:
                        if new_sit[new_row][new_col] in input_info[1:]:
                            like_friend_num += 1
        answer += like_number_score_list[like_friend_num]

print(answer)
