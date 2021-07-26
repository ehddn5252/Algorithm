# 사회적 거리두기를 위해 회의실에 출입할 때 명부를 적어야 한다. 입실과 퇴실이 도시에 이뤄지는 경우는 없다.
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
        meet_people=0
        for j in enter_leave_information:
            if (i[0]>j[0] and i[1]<j[1]) or (i[0]<j[0] and i[1]>j[1]) :
                meet_people+=1
        answer_list.append(meet_people)
    print(answer_list)
    return answer_list

if __name__=="__main__":
    enter=[1,3,2]
    leave=[1,2,3]
    solution(enter,leave)