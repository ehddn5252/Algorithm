import math
if __name__=="__main__":
    
    testcase=int(input())
    for _ in range(testcase):
        floor,room,customerNumber=map(int,input().split())
        # 방문자 수를 층 개수로 나눴을 때 나누어 떨어지는 경우와 안나누어 떨어지는 경우만 나눠서 생각하면 된다.
        # 나눠떨어지는 경우에는 버림해도 값이 같아서 roomNumber가 변하지 않는다. 방문자 수를 층 수로 나누면 방 number가 된다.
        if customerNumber%floor==0:
            roomNumber=customerNumber//floor
            floorNumber=customerNumber-roomNumber*floor
        # 나눠 떨어지지 않는 경우에는 버림하면 roomNumber가 하나 작아지므로 +1을 해줘야 한다.
        # floorNumber를 구할 때는 방문자 수에서 방넘버 * 전체 층수를 빼준 것이 방문자의 층 수가 된다. 
        else:
            roomNumber=customerNumber//floor+1
            floorNumber=customerNumber-(roomNumber-1)*floor
        if roomNumber<10:
            roomNumber=str(0)+str(roomNumber)
        else:
            roomNumber=str(roomNumber)
        if floorNumber==0:
            floorNumber=floor
        answer=str(floorNumber)+roomNumber
        print(answer)
        