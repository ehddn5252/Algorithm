H, W, N, M = map(int, input().split(" "))

left = 1 + (H-1)//(N+1)
down = 1 + (W-1)//(M+1)

ans = left * down
print(ans)

