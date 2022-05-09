def solution(survey, choices):
    for i in range(len(choices)):
        choices[i] -= 4

    # 모든 종류는 8가지
    kind = ["AN", "NA", "CF", "FC", "JM", "MJ", "RT", "TR"]
    a_score = 0
    c_score = 0
    j_score = 0
    r_score = 0
    for i, s in enumerate(survey):
        if survey[i] == kind[0]:
            a_score -= choices[i]

        elif survey[i] == kind[1]:
            a_score += choices[i]

        elif survey[i] == kind[2]:
            c_score -= choices[i]

        elif survey[i] == kind[3]:
            c_score += choices[i]

        elif survey[i] == kind[4]:
            j_score -= choices[i]

        elif survey[i] == kind[5]:
            j_score += choices[i]

        elif survey[i] == kind[6]:
            r_score -= choices[i]

        elif survey[i] == kind[7]:
            r_score += choices[i]

    ret = ""
    if r_score >= 0:
        ret += 'R'
    else:
        ret += 'T'
    if c_score >= 0:
        ret += 'C'
    else:
        ret += 'F'
    if j_score >= 0:
        ret += 'J'
    else:
        ret += 'M'
    if a_score >= 0:
        ret += 'A'
    else:
        ret += 'N'

    return ret


survey1 = ["AN", "CF", "MJ", "RT", "NA"]
choices1 = [5, 3, 2, 7, 5]
print(solution(survey1,choices1))