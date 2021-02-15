


from sys import stdin

if __name__=="__main__":
    subinLocation,brotherLocation=map(int,stdin.readline().split())
    dp1=[0]*10000
    dp2=[0]*10000
    for i in range(subinLocation-1,-1,-1):
        dp1[i]+=1+dp1[i+1]

    for i in range(subinLocation,len(dp1)-1):
        if (i+1)%2==0:
            dp1[i+1]=min(dp1[i],dp1[(i+1)//2])+1
        else:# 이 부분이 문제
            dp1[i+1]=min(dp1[i//2]+2,dp1[i]+1)

    for i in range(subinLocation-1,-1,-1):
        dp2[i]+=1+dp2[i+1]

    for i in range(subinLocation,len(dp2)-1):
        if (i+1)%2==0:
            dp2[i+1]=min(dp2[i],dp2[(i+1)//2])+1
        else:# 이 부분이 문제
            dp2[i+1]=dp2[i]+1
    print(dp1==dp2)