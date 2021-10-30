
# 참고 코드
# https://gurumee92.tistory.com/164

def solution(N, number):
    # 초기 값은 -1로 설정
    answer = -1
    DP = []
    # 1부터 9까지
    for i in range(1, 9):
        # 중복없는 리스트 set
        numbers = set()
        # 숫자를 붙인 수를 더한다. 
        numbers.add( int(str(N) * i) )
        # 각 횟수마다 할 수 있는 모든 경우의 수를 저장
        for j in range(0, i-1):
            # 여기서 DP[j]에 DP[-j-1]을 더하는데 이는 둘이 더하면 같은 횟수가 되게 맞춰주기 위해 사용함
            print(j)
            for x in DP[j]:
                print("DP[j]")
                print(DP[j])
                for y in DP[-j-1]:
                    print("DP[-j-1]")
                    print(DP[-j-1])
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)
                    if y != 0:
                        numbers.add(x // y)
                    if number in numbers: 
                        answer = i
                        print(i)
                        exit() 
        # 정답이 있으면 바로 나감

        '''
        if number in numbers:
            answer = i
            break
        '''
        DP.append(numbers)
    print(DP)
    print(numbers)
    return answer

if __name__ == '__main__':
    N = 5
    number = 12
    result = solution(N, number)
    print(result)