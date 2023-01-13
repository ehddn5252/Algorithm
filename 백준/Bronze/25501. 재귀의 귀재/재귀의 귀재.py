count=0
def recursion(s, l, r):
    global count
    count+=1
    if l >= r:
        return 1

    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


def is_palindrome(s):
    return recursion(s, 0, len(s) - 1)


n = int(input())
start = 0
while start < n:
    count=0
    print(is_palindrome(input()), count)
    start += 1
