# 작성일자 : 20210222
# 문제명 : 나무 자르기

# 문제 풀이 : 잘라야 할 나무의 길이를 이분 탐색의 기준으로 설정한다.

from sys import stdin

def solution(treeList,neededTreeLength):
    answer=0
    start=0
    end = max(treeList)
    while start<=end:
        mid=(start+end)//2
        colletedTreeLenghSum=0
        for treeLength in treeList:
            if mid<treeLength:
                colletedTreeLenghSum+=treeLength-mid
        if colletedTreeLenghSum>=neededTreeLength:
            start=mid+1
            answer=mid
        elif colletedTreeLenghSum<neededTreeLength:
            end=mid-1
    print(answer)



if __name__=="__main__":
    _,neededTreeLength=map(int,stdin.readline().split())
    treeList=list(map(int,stdin.readline().split()))
    solution(treeList,neededTreeLength)