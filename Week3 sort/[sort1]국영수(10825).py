# 작성일 : 20201113
# 작성자 : 김동우
# 문제명 : 국영수
# 문제요약 : 이름, 국, 영, 수 순으로 주어진다.
# 국어 점수가 높은 순, 영어 점수 낮은 순 수학 점수 높은순, 이름 사전순으로 정렬하고 
# 순서대로 이름을 출력하라

a= int(input())
dataList=[]
for i in range(a):
    name,language,english,math = map(str,input().split())
    dataList.append([name,int(language),int(english),int(math)])

dataList.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in dataList:
    print(i[0])
