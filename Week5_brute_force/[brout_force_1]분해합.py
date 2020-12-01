# 작성일 : 20201201
# 작성자 : 김동우
# 문제명 : 분해합
# 문제 요약 :
# 1. 카드 뭉치에서 3장을 골라서 M보다 작거나같은 수를 만들고 그 수를 출력하라.
#  
# 문제 본문은 contents.md 참고 

# 문제 해설 : 
# 처음부터 N까지 돌아본다 1,000,000 까지인데 최댓 자리수가 7이니까 최대 7백만번만 돌면된다.

# 시간 복잡도 : O(7*N)


def solution():
    N=int(input())
    for num in range(1,N):
        editNum=num
        sum=0
        while(editNum>0):
            sum+=editNum%10
            editNum//=10
        if(sum+num==N):
            print(num)
            return
        
            
    print(0)

if __name__ == "__main__":
    solution()