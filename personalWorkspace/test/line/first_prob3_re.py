# 사회적 거리두기를 위해 회의실에 출입할 때 명부를 적어야 한다. 입실과 퇴실이 동시에 이뤄지는 경우는 없다.
# 먼저 왔는데, 나중에 나가는 애들을 찾으면 된다.

# 사람 마다 입실 순서과 퇴실 순서만 기록하자.
# i[0]>j[0] and i[1]<j[1]
def solution(enter, leave):
    
    enter_leave_information=[]
    for _ in range(len(enter)):
        enter_leave_information.append([0,0])

    for enter_index,enter_name in enumerate(enter):
        enter_leave_information[enter_name-1][0]=enter_index

    for leave_index,leave_name in enumerate(leave):
        enter_leave_information[leave_name-1][1]=leave_index
    
    answer_list=[]
    for i in enter_leave_information:
        meet_people=[]
        for j_index,j in enumerate(enter_leave_information):
            if (i[0]>j[0] and i[1]<j[1]):
                meet_people.append(j_index)
        answer_list.append(meet_people)
    #  or (i[0]<j[0] and i[1]>j[1]) :
    for index,value in enumerate(answer_list):
        for j in value:
            for k in answer_list[j]:
                for t in k:
                    answer_list[index].append(t)

    
    for i_index,i in enumerate(enter_leave_information):
        meet_people=[]
        for j_index,j in enumerate(enter_leave_information):
            if (i[0]<j[0] and i[1]>j[1]):
                meet_people.append(j_index)
        for i in meet_people:
            answer_list[i_index].append(i)

    print(answer_list)
    return answer_list

if __name__=="__main__":
    enter=[1,4,2,3]
    leave=[2,1,3,4]
    solution(enter,leave)