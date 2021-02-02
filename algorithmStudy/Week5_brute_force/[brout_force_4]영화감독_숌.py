# 작성일 : 20201202
# 작성자 : 김동우
# 문제명 : 영화감독 숌
# 문제 요약 :
# 1. 카드 뭉치에서 3장을 골라서 M보다 작거나같은 수를 만들고 그 수를 출력하라.
#  
# 문제 본문은 contents.md 참고 

# 문제 해설 : 
# 1. 단순히 1부터 10,000,000까지 돈다
# 2. num이 665이상일 때 도는 while문 생성
# 3. num%1000==666 를 해본다 
# 4. 아니면 num//=10을 한다. 
# 5. 3,4의 과정을 반복하다가 count한 수(endNum)가 입력값과 같은 경우 print, return)

# 시간 복잡도 : O(10,000,000)
# 참고 12>>2 = 12 / 2^2
# 파이썬에서 / 는 실수, //는 정수부 까지 나눈다 참고

def solution():
    N= int(input())
    endNum=0
    # 1. 단순히 1부터 10,000,000까지 돈다
    for num in range(665,10000000):
        editedNum=num
        # 2. num이 665이상일 때 도는 while문 생성

        while (editedNum>665):
            # 3. num%1000==666 를 해본다 
            if editedNum%1000==666:
                endNum+=1
                # 5. 3,4의 과정을 반복하다가 count한 수(endNum)가 입력값과 같은 경우 print, return)
                if endNum==N:
                    print(num)
                    return
                break
            # 4. 아니면 num//=10을 한다. 
            editedNum//=10

if __name__ == "__main__":
    solution()