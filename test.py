# 리모컨

""" 문제요약
1. 현재 채널은 100이고 리모컨에는 버튼이 0~ 9, + 와 - 가 있다.
2. +를 누르면 채널 +1, - 를 누르면 -1로 가고 0에서 -를 누르면 0에서 멈춘다.
3. 어느 버튼이 고장났는 지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을
   최소 몇 번 눌러야 하는 지 구하는 프로그램을 작성하시오

4. 첫째 줄에는 이동하려고 하는 채널이 주어진다.
5. 둘째 줄에는 고장난 버튼의 개수, 3째줄에는 고장난 버튼이 주어진다.
"""

""" 문제풀이
방법1. 
문제를 해결하기 위해서는 숫자 버튼으로 가까이 가는 것이 중요하다.
그래서 있는 버튼 중에서 해당 숫자와 가까운 경우를 확인하고 같은 숫자가 있다면 
선택, 아니라면 뺐을 때, 차이가 가장 작은 숫자를 선택한다.
"""


answer_list=[]
def digit_func(digit_list, digit_index, digit_max, answer):
    if digit_index>=digit_max:
        answer_list.append(answer)
        return

    for num in digit_list[digit_index]:
        answer += str(num)
        digit_func(digit_list,digit_index+1,digit_max,answer)
        answer = answer[:-1]


def solution():
    target_number:str = input()
    answer = abs(int(target_number)-100)
    breakdown_button_num: int = int(input())
    target_len = len(target_number)
    digit_list: list = []
    num_list = []

    activate_buttons = [0,1,2,3,4,5,6,7,8,9]
    if breakdown_button_num!=0:
        deactivate_buttons: list = list(map(int,input().split()))
        for button in deactivate_buttons:
            activate_buttons.remove(button)
    else:
        answer=min(target_len,answer)
    if target_number=="100":
        return 0

    except_case1=""
    except_case2=""
    if not len(activate_buttons)==0:
        if len(activate_buttons)==1 and activate_buttons[0]==0:
            pass
        else:
            for i in range(target_len):
                if i==0 and activate_buttons[0]==0:
                    except_case1+=str(activate_buttons[1])
                else:
                    except_case1+=str(activate_buttons[0])
            except_case1+=str(activate_buttons[0])
            answer_list.append(except_case1)
        if len(activate_buttons)!=1 and target_len!=1:
            for i in range(target_len):
                if i==0:
                    continue
                except_case2+=str(activate_buttons[-1])
            answer_list.append(except_case2)

    for part_number in target_number:
        difference_list=[]
        answer_candidate: list= []
        for active_button in activate_buttons:
            diff = abs(active_button- int(part_number))
            difference_list.append(diff)

        for active_button in activate_buttons:
            diff = abs(active_button- int(part_number))
            if diff in difference_list:
                answer_candidate.append(active_button)
        num_list.append(len(answer_candidate))
        digit_list.append(answer_candidate)

    digit_max = len(digit_list)
    
    digit_func(digit_list,0,digit_max,"")
    min_value = 500000
    saved_num = 0
    target_number = int(target_number)
    for num in (answer_list):
        diff = abs(int(num)-target_number)
        if diff<min_value:
            min_value= diff
            saved_num = num
    if answer > min_value+len(str(saved_num)):
        answer = min_value+len(str(saved_num))

    return answer
    # 여기에서 모든 숫자를 조합해서 차이가 최소가 되는 것을 만들면 된다.
    # 시간은 O(2^6) 걸린다.
    # 조합 만드는 방법:
    """
    쉬운 방법으로는 각 자리마다 자릿수를 고정해놓는 것이다. 
    그렇지만 자릿수를 고정해놓으면 재사용성이 떨어지므로 자릿수를 고정하지 않아도 되는 로직을 만들어야 한다.
    
    각 자릿수마다 숫자가 있는 2차원 리스트 digit_list가 있다.
    digit_list의 각 리스트의 개수는 모른다.
    그 자릿수마다 내부로 재귀로 들어가서 결과에 append하는 재귀문을 만들어야 한다.
    """


if __name__=="__main__":
    print(solution())