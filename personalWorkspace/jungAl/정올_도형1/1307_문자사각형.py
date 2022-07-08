alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"]

n = int(input())

for i in range(n-1,-1,-1):
    for j in range(n*(n-1),-1,-n):
        # print(str(i+j)+" ",end="")
        print(alphabets[(i+j) % len(alphabets)]+" ", end="")
    print("")