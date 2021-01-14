
def solution():
    computerNum=int(input())
    entireConnection=[]
    for i in range(computerNum):
        entireConnection.append(0)
    connectNum=int(input())
    computerConnection=[]
    for _ in range(connectNum):
        inputTmp=list(map(int,input().split()))
        computerConnection.append(inputTmp)
    flag=1
    for i in computerConnection:
        computer1=entireConnection[i[0]-1]
        computer2=entireConnection[i[1]-1]
        entireConnection[i[1]-1]=flag
        entireConnection[i[0]-1]=flag
        for index,value in enumerate(entireConnection):
            if computer1!=0 and value==computer1:
                entireConnection[index]=flag
            if computer2!=0 and value==computer2:
                entireConnection[index]=flag
        flag+=1

    answer=0
    for index,value in enumerate(entireConnection):
        if index==0:
            continue
        if value==entireConnection[0]:
            answer+=1
    print(answer)
if __name__ == "__main__":
    solution()