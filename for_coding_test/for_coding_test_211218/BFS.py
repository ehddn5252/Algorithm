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


target_number:str = input()
breakdown_button_num: int = int(input())
deactivate_buttons: list = list(map(int,input().split()))
digit_list: list = []
num_list = []

activate_buttons = [0,1,2,3,4,5,6,7,8,9]
for button in deactivate_buttons:
    activate_buttons.remove(button)

for part_number in target_number:
    min_difference=9
    answer_candidate: list= []
    for active_button in activate_buttons:
        diff = active_button- int(part_number)
        if diff<min_difference:
            min_difference = diff

    for active_button in activate_buttons:
        diff = active_button- int(part_number)
        if diff==min_difference:
            answer_candidate.append(active_button)
    num_list.append(len(answer_candidate))
    digit_list.append(answer_candidate)

# 여기에서 모든 숫자를 조합해서 차이가 최소가 되는 것을 만들면 된다.
# 시간은 O(2^6) 걸린다.
# 조합 만드는 방법:
"""
answer_list에는 각 자릿수에 적합한 숫자가 있다.
각 자릿수별로 모든 숫자를 조합해야 한다. 
그러면 최대 자릿수를 먼저 얻어내고 각 자릿수별로 answer를 만들고 answer_list에 추가한다.

"""

from  itertools import product

print(list(product(digit_list)))
