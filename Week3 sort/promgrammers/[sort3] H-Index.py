# 어떤 과학자가 발표한 논문 n편 중 h번 이상 인용된 논문이 h편 이상이고, 
# 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index이다.
# 구현 방법 :
# 예시. 만약 논문 [5,4,3,2,1] 이라면 3번 이상 인용된 논문이 3편 이상이다.
# 확인하는 방법은  큰 값부터 시작해서 그 값보다 크거나 같은 수가 그 수 이상인지 확인해야한다.
# 삽질 :
# citations의 크기서부터 0까지 확인해야하는데,  citations의 크기서부터 1까지 확인했다.

citations = [3, 0, 6, 1, 5]

def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations),-1,-1):
        numberOfTimesCited=0
        for j in range(len(citations)):
            if i<=citations[j]:
                numberOfTimesCited+=1
        if numberOfTimesCited>=i and len(citations)-numberOfTimesCited<=i:
            return i