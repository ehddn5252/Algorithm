import sys

N, M = map(int, input().split(" "))

keywords = {}
for _ in range(N):
    keywords[sys.stdin.readline()[:-1]] = 0
for _ in range(M):
    writings = sys.stdin.readline()[:-1].split(",")
    for write in writings:
        if keywords.get(write) is not None:
            keywords.pop(write)
    print(len(keywords))
