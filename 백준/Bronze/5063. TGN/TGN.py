
n = int(input())
for _ in range(n):
    r, e, c = map(int,input().split(" ")) # 광고를 하지 않았을 때 수익, 광고를 했을 때의 수익, 광고 비용
    if r+c==e:
	    print("does not matter")
    elif r+c<e:
        print("advertise")
    else:
        print("do not advertise")    
