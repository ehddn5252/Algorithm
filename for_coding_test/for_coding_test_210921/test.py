'''
DFS와 BFS를 사용한다.
DFS는 깊이 우선 탐색
BFS는 넓이 우선 탐색이다.

깊이 우선 탐색을 할 때에는 스택을 사용한다.
1. 한 점을 정한다. (시작점)
2. 연결된 모든 주변 지역을 스택에 넣는다.
3. 스택에 pop을 한다. pop을 하면서 그 곳을 지난다고 기록한다.
4. pop을 한 점을 기준으로 정하고 주변 모든 지역을 스택에 넣는다.
5. 스택이 빌때까지 3,4를 반복하면 완성

넓이 우선 탐색을 할 때에는 큐를 사용한다. 
1. 한 점을 정한다. (시작점)
2. 연결된 모든 주변 지역을 큐에 넣는다.
3. 큐를 pop한다. pop을 하면서 그 곳을 지난다고 기록한다.
4. pop을 한 점을 기준으로 정하고 주변 모든 지역을 queue에 넣는다.
5. 큐가 빌 때까지 3,4,를 반복하면 완성


'''

import math
def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if str2[i:i+2].isalpha()]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)


'''
위 코드에서는 컴프리핸션을 사용해 매우 간결하게 짰고 길이를 마지막 str1-1까지로 두어서 
str1[i:i+2]를 돌린다면 마지막이 str1-2까지 가서 dangling pointer로 runtime error가 나지 않는다.
lower(), isalpha(), count로 파이썬 내장 라이브러리를 사용하여 기능 구현을 했다.
특히 count 함수는 문자열 내에 특정 단어가 몇 번 나타나는 지 알려주어 매우 효율적이라 생각된다

& 로 inner join, |을 사용해 outer join을 구현했다.
math.floor을 사용해서 버림을 구현했는데, 글자 그대로 구현한 것이다.

글자를 정확하게 읽고 간결하고 깔끔한 코드를 짜는 것이 중요한 데, 그것을 그대로 행한 것이다.
'''
