def solution():
    N= int(input())
    person=[]
    for i in range(N):
        person.append(list(map(int,input().split())))

    for i in range(N):
        person[i].append(i)
    print(person)


if __name__ == "__main__":
    solution()