n = int(input())
s = input()
a_count = 0
b_count = 0
for i in range(n):
    if s[i] == 'A':
        a_count += 1
    else:
        b_count += 1

if a_count > b_count:
    print("A")
elif a_count < b_count:
    print("B")
else:
    print("Tie")
