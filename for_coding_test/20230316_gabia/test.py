from itertools import combinations

from itertools import combinations


def solution(dots, lines):
    # 가능한 선분 조합 구하기
    line_combinations = []
    for i in range(1, len(lines) + 1):
        line_combinations.extend(combinations(lines, i))

    # 가능한 선분 조합으로 점들을 덮을 수 있는지 확인하고 최소 개수 구하기
    min_count = len(dots)
    for line_set in line_combinations:
        used_lines = set()
        count = 0
        for i in range(len(dots) - 1):
            distance = dots[i + 1] - dots[i]
            for line in sorted(line_set, reverse=True):
                if distance <= line and line not in used_lines:
                    count += 1
                    break
        # 모든 점을 덮을 수 있는 경우
        if count < min_count:
            min_count = count

    # 모든 조합으로도 덮을 수 없는 경우
    if min_count == len(dots):
        return -1
    else:
        return min_count

a,b = [1, 5, 8], [1, 3, 4, 6]

print(solution(a,b))