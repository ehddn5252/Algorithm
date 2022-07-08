alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"]

n = int(input())
if n<1 or n>100 or n%2==0:
    print("INPUT ERROR")
    exit(0)

if n == 1:
    print(alphabets[0])
else:
    num = (n//2+1)**2-n
    for i in range(n):
        tmp_sum = 0
        for j in range(n):
            if j!=0:
                tmp_sum+=n-(2*j)+1
            else:
                tmp_sum=0
            if i <= n/2:
                if j > i:
                    print("  ", end="")
                else:
                    print(alphabets[(num+i-tmp_sum) % len(alphabets)]+" ", end="")
            else:
                if j >= n-i:
                    print("  ", end="")
                else:
                    print(alphabets[(num+i-tmp_sum) % len(alphabets)]+" ", end="")
        print("")