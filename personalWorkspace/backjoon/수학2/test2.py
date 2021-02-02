import math

if __name__=="__main__":
    testcase= int(input())
    # (x1,y1) 반지름 r1 이고 (x2,y2) 반지름 r2인 두 원의 접점 수를 찾으면 된다.
    for i in range(testcase):
        x1,y1,r1,x2,y2,r2=map(int,input().split())
        distanceChoAndBack=math.sqrt((x1-x2)**2+(y1-y2)**2)
        # 무한대인 경우 중심이 같고 반지름이 같을 때
        if x1==x2 and y1==y2 and r1==r2:
            print(-1)
        # 중심이 같고 반지름이 다를 때 or 두 원의 중심 사이 거리가 반지름의 합보다 클때 or 한 원이 다른 원 안에 있을 떄
        elif (x1==x2 and y1==y2 and r1!=r2) or distanceChoAndBack>r1+r2 or abs(r1-r2)>distanceChoAndBack:
            print(0)
        # 내접원 조건과 외접원 조건
        elif r1+r2==distanceChoAndBack or abs(r1-r2)==distanceChoAndBack:
            print(1)
        # 그 외 모두 2라고 보면 된다.
        elif r1+r2>distanceChoAndBack:
            print(2)