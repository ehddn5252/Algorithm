# 작성일자 : 20210202
# 문제명 : 파일 합치기
# 문제 풀이 : do[i-1]가 file보다 작으면 ㄱㅊ
# 어렵네.. 일단 pass

import sys



def solution(num,fileList):
    dp=[0]*num
    fileList.sort()
    dp[0]=fileList[0]
    dp[1]=fileList[1]+dp[0]
    for i in range(2,num):
        dp[i]=min(dp[i-2]+fileList[i-1],dp[i-2]+fileList[i-1]+fileList[i])
    print(dp)


if __name__=="__main__":
    testcase= int(sys.stdin.readline())

    for i in range(testcase):
        num=int(sys.stdin.readline())
        fileList=list(map(int,sys.stdin.readline().split()))
        solution(num,fileList)