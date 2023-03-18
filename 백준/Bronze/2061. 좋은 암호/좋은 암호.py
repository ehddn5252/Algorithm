K, L = map(int,input().split(" "))

for i in range(2,K):
    if K%i==0 and i<L:
        print(f"BAD {i}")
        exit(0)
    if i>=L:
        break
print("GOOD")