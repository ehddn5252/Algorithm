from itertools import permutations
test_case_num = int(input())

for test_case_index in range(1,test_case_num+1):
    N = int(input())
    l = []
    for i in range(N):
        l.append(list(map(int,input().split(" "))))
    ans = 0
    for i in permutations(range(N),N):
        multi = 1
        for j in range(N):
            if(l[j][i[j]]==0):
                break
            multi*=l[j][i[j]]*0.01

        if(multi>ans):
            ans=multi
    ans*=100
    print(f"#{test_case_index} {round(ans,6)}")


