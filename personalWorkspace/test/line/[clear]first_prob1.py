'''
table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]

languages = ["PYTHON", "C++", "SQL"]

preference = [7, 5, 5]

문제 풀이 순서 :

1. split으로 분리한다. 
2. 분리한 언어가 있을 경우 그 인덱스에 값을 곱하고 더한다.
3. 
'''

# 개발자가 사용하는 언어와 언어 선호도를 입력하면 그에 맞는 직업군을 추천해주는 알고리즘 개발하려한다.
# 언어 선호도 x 직업군 언어 점수의 총합이 가장 높은 직업군을 return하도록한다.

def solution(table, languages, preference):
    ansList=[]
    value_table=[0,5,4,3,2,1]
    for table_mini in table:
        ansList.append(table_mini.split())
    answer=[]
    for ans in ansList:
        ansSum=0
        for index,value in enumerate(ans):
            for lan_index,language in enumerate(languages):
                if value==language:
                    ansSum+=preference[lan_index]*value_table[index]
        answer.append([ans[0],ansSum])
    answer.sort(key=lambda x:(-x[1],x[0]))
    #print(answer)
    return answer[0][0]

