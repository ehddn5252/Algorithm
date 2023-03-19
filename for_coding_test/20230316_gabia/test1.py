import copy

def solution(K, user_scores):
    answer = 0
    before = []
    rank = []
    for i, user_score in enumerate(user_scores):
        before = copy.deepcopy(rank[:K])
        is_change = False
        name, score = user_score.split(" ")
        score = int(score)
        for j in range(len(rank)):
            if rank[j][2] == name:
                is_change = True
                if rank[j][0] < score:
                    rank[j][0] = score
                    rank[j][1] = i
                break

        if not is_change:
            rank.append([score, i, name])

        rank.sort(key=lambda x: (-x[0], x[1]))
        rank = rank[:K]
        if len(rank)!=len(before):
            answer += 1
        else:
            for k, (_, _) in enumerate(zip(before, rank)):
                if before[k][2] != rank[k][2]:
                    answer += 1
                    break

    return answer
