a = int(input())
b = list(map(int, input().strip().split(" ")))
c = int(input())

multiples = 0
dividors = 0

for i in b:
    if c % i == 0:
        dividors += i
    if i % c == 0:
        multiples += i
print(dividors)
print(multiples)


