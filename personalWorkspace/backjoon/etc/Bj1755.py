
def num_to_string(num):
    global alphabet_string
    digit_one = num % 10
    digit_two = num//10
    if num>=10:
        return alphabet_string[digit_two] + " "+alphabet_string[digit_one]
    else:
        return alphabet_string[digit_one]

if __name__ == "__main__":
    alphabet_string = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    M, N = map(int, input().split(" "))
    new_l = []
    for i in range(M, N+1):
        new_l.append([num_to_string(i),i])
    new_l.sort(key=lambda x:x[0])
    for i,v in enumerate(new_l):
        if(i!=0 and i%10==0):
            print("")
        print(str(v[1])+" ",end="")