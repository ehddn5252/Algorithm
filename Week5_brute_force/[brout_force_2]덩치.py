# 작성일 : 20201201
# 작성자 : 김동우
# 문제명 : 덩치
# 문제 요약 :
# 1. 몸무게와 키의 리스트가 주어진다.
# 2. A의 몸무게와 키 둘다 B보다 작을경우, 덩치 등수가 낮다.(1등이 젤 높음)
# 3. A의 몸무게가 B보다 크고 B의 키가 A보다 큰 경우는 덩치 등수가 같다.
# 4. 덩치순위를 나열하라.
# 문제 본문은 contents.md 참고 

# 문제 해설 : 
# 1. index를 순서대로 append한다
# 2. 
# 시간 복잡도 : O(N^3)

def solution():
    N= int(input())
    person=[]
    for i in range(N):
        person.append(list(map(int,input().split())))
    for i in range(N):
        person[i].append(i)

    rank=1
    stack=0
    person.sort(key=lambda x:(-x[0]))
    personSize=len(person)
    for pivot in range(0,personSize-1):
        person[pivot].append(rank)
        if(person[pivot][1]>person[pivot+1][1]):
            rank+=1+stack
            stack=0
        else:
            stack+=1

    person[personSize-1].append(rank)
    person.sort(key=lambda x:(x[2]))
    ans=""
    for i in person:
        ans+=str(i[3])
        if(i!=person[-1]):
            ans+=" "
    print(ans)


if __name__ == "__main__":
    solution()