# 작성일자 : 20210215
# 문제명 : 나는야 포켓몬 마스터 이다솜
# 문제 요약 : 
# 문제 풀이 : 해시 dic 사용

from sys import stdin


if __name__=="__main__":
    num,times=map(int,stdin.readline().split())
    pocketmonDic={}
    for i in range(1,num+1):
        pocketmon=stdin.readline().strip()
        pocketmonDic[str(i)]=pocketmon
        pocketmonDic[pocketmon]=str(i)
    for _ in range(times):
        pocketmon=stdin.readline().strip()
        print(pocketmonDic[pocketmon])

