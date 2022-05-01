import sys
sys.setrecursionlimit(2000)
print= sys.stdout.write

def solution():
    global dp, l
    # N은 안쓰임
    N = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    for i in range(M):
        start, end = map(int, sys.stdin.readline().split())
        if (check_palindrom(start-1,end-1)):
            print("1\n")
        else:
            print("0\n")

def check_palindrom(s,e):
    global l
    if(s>=e):
        return True

    if (l[s]==l[e]):
        return check_palindrom(s+1, e-1)
    else:
        return False

if __name__ == "__main__":
    solution()
