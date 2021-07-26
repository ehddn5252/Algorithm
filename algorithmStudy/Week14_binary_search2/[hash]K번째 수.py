# 작성 일자 : 20210222
# 문제명 : K번째 수
# 문제 요약 : 
# 1. 세준이는 크기가 N x N인 배열 A를 만들었다. 
# 2. 배열에 들어있는 수 A[i][j]=i x j 이다.
# 3. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N x N이 된다. 
# 4. B를 오름차순 정렬했을 때 B[k]를 구해보자.


# 문제 풀이 :
# 1. (1 * 1 2 * 1 + .. + n * 1 )+ (1 * 2 + 2 * 2 + .. + n * 2) + ... (n * 1 n * 2 + .. + n * n) 데이터를 만들어야 한다.
# 1-1. 이는 2중 for문으로 최대 100,000,000 회 돌자.
# 2. 해시 사용 해시를 사용해서 중복되는 것을 저장하면 메모리를 아낄 수 있다.
# 3. 
from sys import stdin

def solution(arraySize,K):
    dictionaryValue={}
    valueK=K
    for i in range(1,arraySize+1):
        for j in range(1,arraySize+1):
            if dictionaryValue.get(i*j,0)!=0:
                dictionaryValue[i*j]+=1
            else:
                dictionaryValue[i*j]=1

    for i in range(K+1):
        if dictionaryValue.get(i,0)==0:
            continue
        else:
            valueK-=dictionaryValue[i]
        if valueK<=0:
            print(i)
            return




    


if __name__=="__main__":
    arraySize=int(stdin.readline().strip())
    K=int(stdin.readline().strip())
    solution(arraySize,K)
