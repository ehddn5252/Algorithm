testcase = int(input())

for _ in range(testcase):
    tmp=0
    score =0
    n = int(input())
    for _ in range(n):
        a,m = map(float,input().split())
        tmp+=a
        score +=m*a
    print(f"{int(tmp)} {score/tmp:.1f}")