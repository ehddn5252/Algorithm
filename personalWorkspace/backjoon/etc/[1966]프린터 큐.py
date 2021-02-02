# 작성일자 20210201
# 문제명 : 백준 [1966] 프린터 큐
# 문제 풀이 :
# 문제에서 말한 그대로 구현하면 된다.
# https://www.acmicpc.net/problem/1966 
import sys
def solution(n,order,printList):
    answer=0
    orderList=[]
    for i in range(len(printList)):
        orderList.append(i)
    i=0
    while True:
        if max(printList)==printList[i]:
            answer+=1
            if order==orderList[i]:
                print(answer)
                return
            del printList[i]
            del orderList[i]
        else:
            deletedPrintListElement=printList[i]
            deletedOrderListElement=orderList[i]
            del printList[i]
            del orderList[i]
            printList.append(deletedPrintListElement)
            orderList.append(deletedOrderListElement)

if __name__=="__main__":
    testCase=int(sys.stdin.readline())
    for i in range(testCase):
        n,order=map(int,sys.stdin.readline().split())
        printList=list(map(int,sys.stdin.readline().split()))
        solution(n,order,printList)