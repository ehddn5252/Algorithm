# 작성일 : 20201113
# 작성자 : 김동우
# 문제명 : 나이순 정렬
# 문제요약 : 나이작은순으로 정렬한다. 같으면 등록순으로 정렬한다.


a= int(input())
dataList=[]
for i in range(a):
    age,name = map(str,input().split())
    dataList.append([int(age),name])

dataList.sort(key=lambda x:(x[0]))

for i in dataList:
    print(i[0], i[1])
