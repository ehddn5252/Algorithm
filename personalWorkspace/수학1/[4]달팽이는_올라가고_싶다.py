import math

if __name__=="__main__":
    up,down,high=map(int,input().split())
    onedayUp=up-down
    # 맨 마지막에는 올라가서 안내려오니까 up을 맨처음 하나 빼준다.
    high-=up
    day=math.ceil(high/onedayUp)
    print(day+1)


