import copy

def solution(costs,xcost,ycost):
    answer=-1
    dp_list:list = copy.deepcopy(costs)
    print(dp_list)
    for row in range(len(costs)):
        for col in range(len(costs[0])):
            if col==0 and row==0:
                continue
            if col==0:
                dp_list[row][col] = dp_list[row-1][col]+dp_list[row][col]-ycost
            elif row==0:
                dp_list[row][col] = dp_list[row][col-1]+dp_list[row][col]-xcost
            else:
                dp_list[row][col]=max(dp_list[row-1][col]+dp_list[row][col]-ycost,dp_list[row][col-1]+dp_list[row][col]-xcost)
    answer = max(dp_list[len(costs)-1])
    if answer<0:
        answer=0

    return answer