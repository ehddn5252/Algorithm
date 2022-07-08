alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"]

n = int(input())
for i in range(0, n):
    for j in range(0,n*n,n):
        if (j/n) % 2 == 0:
            print(alphabets[(j+i)%26]+" ", end="")
            #print(str(j+i)+" ", end="")
        else:
            print(alphabets[(j+(n-i-1))%26]+" ",end="")
            #print(str(j+(n-i+1))+" ", end="")
    print("")
