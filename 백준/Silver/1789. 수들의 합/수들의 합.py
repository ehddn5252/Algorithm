n = int(input())

start=1
sum_value=0
while True:
    sum_value+=start
    if sum_value>n:
        print(start-1)
        break
    elif sum_value==n:
        print(start)
        break
    start+=1