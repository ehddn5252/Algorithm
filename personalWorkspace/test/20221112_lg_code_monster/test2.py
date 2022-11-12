import itertools

def solution(marbles):
    answer_list = []
    marbles.sort()
    marble_len = len(marbles)
    for marble_size in range(marble_len-1, 0, -1):
        for j in itertools.permutations(marbles, marble_size):
            middle = int(len(j) / 2)
            front = sum(j[:middle])
            back = sum(j[middle:])
            if front == back:
                answer_list.append(j)

        if marble_size==marble_len-1:
            for j in itertools.permutations(marbles, marble_size+1):
                middle = int(len(j) / 2)
                front = sum(j[:middle])
                back = sum(j[middle:])
                if front == back:
                    answer_list.append(j)

    answer=[]
    print(answer_list)
    for i in answer_list:
        if(len(i)%2==0):
            answer = i
            for j in i:
                if j in marbles:
                    marbles.remove(j)
            break

    if answer==[]:
        if len(answer_list)!=0:
            answer = answer_list[0]
            for i in answer_list[0]:
                if i in marbles:
                    marbles.remove(i)

    answer_type_list = list(answer)
    if(len(marbles)!=0):
        middle = int(len(answer_type_list)/2)
        answer_type_list.insert(middle,max(marbles))

    print(answer_type_list)

    return answer_type_list


marbles = [1, 2, 3, 4, 4, ]
marbles2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
marbles3 = [5,5,1,4]
marbles4 = [3,9,5,7]
marbles5 = [7,3,1]
solution(marbles)
