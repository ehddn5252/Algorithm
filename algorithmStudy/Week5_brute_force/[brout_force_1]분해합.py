# 작성일 : 20201201
# 작성자 : 김동우
# 문제명 : 분해합
# 문제 요약 :

# 문제 본문은 contents.md 참고 

# 문제 해설 : 

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