# four square answer
n = int(input())
min_sum = 4 #최대는 4라고 증명되어있다, 아래 3중 for문에서 걸리지 않는다면 답은 4
for a in range(int(n**0.5), int((n//4)**0.5), -1): #가능한 최소한의 범위로 축소해준다
    if a*a == n:
        min_sum = 1 #최소의 숫자일 경우
        break
    else:
        temp = n - a*a
        for b in range(int(temp**0.5), int((temp//3)**0.5), -1): #남은 숫자는 3이니까 3으로 나누어줌
            if a*a + b*b == n:
                min_sum = min(min_sum, 2)
                continue
            else:
                temp = n - a*a - b*b
                for c in range(int(temp**0.5), int((temp//2)**0.5), -1):
                    if n == a*a + b*b + c*c:
                        min_sum = min(min_sum, 3)
                
print(min_sum)