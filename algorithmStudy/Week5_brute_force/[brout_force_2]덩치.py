# 작성일 : 20201202
# 작성자 : 김동우
# 문제명 : 덩치
# 문제 요약 :
# 1. 몸무게와 키의 리스트가 주어진다.
# 2. A의 몸무게와 키 둘다 B보다 작을경우, 덩치 등수가 낮다.(1등이 젤 높음)
# 3. A의 몸무게가 B보다 크고 B의 키가 A보다 큰 경우는 덩치 등수가 같다.
# 4. 덩치순위를 나열하라.
# 문제 본문은 contents.md 참고 

# 문제 해설 : 
# 1. 1등부터 시작해서 덩치와 키가 둘 다 작은 경우에 등수를 하나씩 올린다.
# 2. 맨 마지막에 등수를 ansList에 추가한다.
# 시간 복잡도 : O(N^2)

def solution():
    N= int(input())
    person=[]
    for i in range(N):
        person.append(list(map(int,input().split())))
        
    ansList=[]
    personSize=len(person)
    for pivot in range(0,personSize):
        rank=1
        for compare in range(0,personSize):
            if (person[pivot][0] < person[compare][0]) and (person[pivot][1] < person[compare][1]):
                rank+=1
        ansList.append(rank)
    ans=""
    for i in ansList:
        ans+=str(i)
        ans+=" "
    print(ans)


if __name__ == "__main__":
    solution()