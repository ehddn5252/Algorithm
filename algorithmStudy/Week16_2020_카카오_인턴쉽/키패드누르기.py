# 작성 일자 : 20210312
# 문제 명 : 키패드 누르기
# 문제 요약 : 
# 1. 왼쪽 엄지는  *에 오른쪽 엄지는 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙
# 2. 왼쪼 열의 1,4,7을 입력할 때는 왼손 엄지손가락을 사용
# 3. 오른쪽 열의 3,6,9를 입력할 때는 오른손 엄지손가락을 사용.
# 4. 가운데 열의 4개 숫자를 입력할 때는 두 엄지 중 가까운 엄지손가락 사용
# 4-1. 거리가 같다면 오른손잡이는 오른손 왼손잡이는 왼손 엄지를 사용

# 입력 : 순서대로 누를 번호가 담긴 배열 numbers, 오른손잡이, 왼손잡이 인지 확인하는 손,  

# phone array 
#     0 1 2
#0 [ [ 1 2 3 ]
#1   [ 4 5 6 ]
#2   [ 7 8 9 ]
#3   [ * 0 # ] ]


def solution(numbers, hand):
    answer = ''
    phoneKeypad=[[1,3],[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]]
    leftHand=[0,3]
    leftCalcu=0
    rightHand=[2,3]
    rightCalcu=0
    for number in numbers:
        if number==1:
            leftHand=phoneKeypad[1]
            answer+="L"
        elif number==4:
            leftHand=phoneKeypad[4]
            answer+="L"
        elif number==7:
            leftHand=phoneKeypad[7]
            answer+="L"
        elif number==3:
            rightHand=phoneKeypad[3]
            answer+="R"
        elif number==6:
            rightHand=phoneKeypad[6]
            answer+="R"
        elif number==9:
            rightHand=phoneKeypad[9]
            answer+="R"
        else:
            leftCalcu=abs(phoneKeypad[number][0]-leftHand[0])+abs(phoneKeypad[number][1]-leftHand[1])
            rightCalcu=abs(phoneKeypad[number][0]-rightHand[0])+abs(phoneKeypad[number][1]-rightHand[1])
            if hand=="right":
                if leftCalcu>=rightCalcu:
                    rightHand=phoneKeypad[number]
                    answer+="R"
                else:
                    leftHand = phoneKeypad[number]
                    answer+="L"
            elif hand=="left":
                if leftCalcu<=rightCalcu:
                    leftHand = phoneKeypad[number]
                    answer+="L"
                else:
                    rightHand = phoneKeypad[number]
                    answer+="R"
        #print(f'phoneKeypad[number] : {phoneKeypad[number]}, number : {number},leftHand = {leftHand}, rightHand = {rightHand} leftCalcu={leftCalcu},rightCalcu={rightCalcu},')
    return answer



if __name__=="__main__":
    numbers =[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand="left"

    solution(numbers,hand)