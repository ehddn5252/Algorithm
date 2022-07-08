alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"]

n = int(input())
for i in range(0, n):
    count = 0

    for j in range(0,n):
        if i+j<n-1:
            print("  ", end="")
        else:
            tmp_sum=0
            for k in range(count):
                tmp_sum += n-k-1
            print(alphabets[(i+tmp_sum)%26]+" ",end="")
            count+=1
    print("")
