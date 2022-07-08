N, K = map(int,input().split(" "))

'''
10,1 : 10
10,2 : 2부터 시작해서 2 4 6 8 10 으로 올라간다. 10이 최악의 숫자라고 생각하면 2 4 6 8 10 9 6 번

4,2 : 2 4 3 총 3번

8, 3: 3 6 8 7

88 7
F = 85 라고 하자
84 까지 12번
88 깨짐
86 깨짐
85 
15번 


94 90

1+
90
45
23
12
6
3
1



100 10
10 20 30 40 50 60 70 80 90 99
95 93 92 91

10 5
5 10 8 6 7

300 20
'''
times = int(N/K)
tmp=1
next_times=0
while tmp<K:
    tmp*=2
    next_times+=1
#ret = max(times+int((N-K*times)/2)+1,times+next_times)
ret = times+next_times
if K==1:
    ret=N

print(ret)