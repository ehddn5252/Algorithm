# 작성일 : 20201119,20
# 작성자 : 김동우
# 문제명 : 가장 긴 증가하는 부분 수열2
# 문제 요약 : 
# 1. 수열 A가 주어진다.
# 2. 가장 긴 증가하는 부분 수열을 구하는 프로그램 작성
# ex1) A={50,10,30,20,40} 이면 3 ({10,30,40}) 이 답이 된다.
# ex2) A={30,40,50,20,40,60} 이면 4({30,40,50,60}) 이 답이 된다.
# 문제 본문은 contents.md 참고 

# 문제 해석 :
# 방법 1
# 1. 가장 긴 수열을 찾기 위해서는 부분 수열을 만든다.
# 2. 그 수열 중 증가하는 수열을 추린다.
# 3. 가장 길이가 긴 것을 찾는다.

# 부분수열 만들때 시간복잡도가 O(2^N)이 걸린다. (부분 수열 만드는 부분의 시간 복잡도를 줄여야 한다)

# 방법 2 부분 수열을 만들 때 시간을 줄여야 한다.
# 1. 주어진 수열을 처음부터 끝까지 검색한다.
# 2. 만약  리스트가 비어있으면 현재 위치의 NUM을 리스트에 추가한다.
# 3. 리스트의 마지막 index의 수가 num보다 작으면 리스트에 추가한다.
# 4. 리스트의 마지막 index의 수가 num보다 크거나 같으면 lower_bound 함수로 들어간다. 
# 5. num보다 큰 수 중 가장 작은 값의 인덱스을 찾고 그 값 자리에 num을 넣는다. 
# lower_bound는 subsequenceList에서 num을 찾거나 num보다 큰 수 중 가장 작은 수의 인덱스를 return한다.

# 시간 복잡도 : O(Nlog_2(N))

# 왜냐하면 증가하는 부분 수열 중 가장 긴 배열을 찾기 위해서는 최소 값이 있다면 그 값으로 바꿔줘야 한다.
# 예시를 보면 이해가 쉽다. 배열{1,2,4,8,7,6,8}이 주어지면 0번째(1)에서 3번째 인덱스(8)까지 탐색한 상황에서 
# subsequenceList는 {1,2,4,8}가 된다. 여기서 subsequenceList[-1]인 8과 4번째 인덱스 7을 비교한다.
# 8보다 7이 작으므로 7보다 큰 수중 가장 작은 수를 찾아 그 수가 있는 자리에 7을 넣어준다.
#  {1,2,4,8} -> {1,2,4,7}
# 5번째 인덱스 6이 들어올 차례다. 6이 7보다 작으므로 6보다 큰 수중 가장 작은 수를 찾아 그 자리에 6을 넣는다.
#  {1,2,4,7} -> {1,2,4,6}
# 6번째 인덱스 8이 들어온다. 그대로 8을 넣어준다. 
# {1,2,4,6} -> {1,2,4,6,8} 
# {1,2,4,8,3,5,8}
# { 1 2 3 5 8 }

# lower_bound는 subsequenceList에서 num을 찾거나 num보다 큰 수 중 가장 작은 수의 인덱스를 return한다.

def lower_bound(subsequenceList,num):
    start=0
    end=len(subsequenceList)-1
    # end가 start보다 작아지면 그때의 end값이 lower bound이다
    while start<end:
        mid=(start+end)//2
        if subsequenceList[mid]<num:
            start=mid+1
        else:
            end=mid
    return end

def solution():
    garbage=int(input())
    inputedList=[]
    inputedList=list(map(int,input().split()))
    subsequenceList=[]

    # 1. 주어진 수열을 처음부터 끝까지 검색한다.
    for num in inputedList:
        # 2. 만약  리스트가 비어있으면 현재 위치의 NUM을 리스트에 추가한다.
        if len(subsequenceList)==0:
            subsequenceList.append(num)

        # 3. 리스트의 마지막 index의 수가 num보다 작으면 리스트에 추가한다.
        if subsequenceList[-1]<num:
            subsequenceList.append(num)
        # 4. 리스트의 마지막 index의 수가 num보다 크거나 같으면 lower_bound 함수로 들어간다. 
        else: #subsequenceList[-1]>=num:
            # 5. num보다 큰 수 중 가장 작은 값의 인덱스을 찾고 그 값 자리에 num을 넣는다. 
            index= lower_bound(subsequenceList,num)
            subsequenceList[index]=num

    print(len(subsequenceList))


if __name__ == "__main__":
    solution()