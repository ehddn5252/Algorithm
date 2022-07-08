N = int(input())

ans = 0
for i in range(N):
    student_num, apple_num = map(int,input().split(" "))
    ans+= apple_num % student_num

print(ans)