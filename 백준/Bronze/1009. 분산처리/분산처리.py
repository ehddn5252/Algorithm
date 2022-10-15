testcase_num = int(input())
l = [[10, 10, 10, 10]]
for i in range(1, 10):
    l.append([i, (i * i) % 10, (i * i * i) % 10, (i * i * i * i) % 10])
    
for i in range(testcase_num):
    a, b = map(int, input().split(" "))
    a = a % 10
    b = (b - 1) % 4
    print(l[a][b])
