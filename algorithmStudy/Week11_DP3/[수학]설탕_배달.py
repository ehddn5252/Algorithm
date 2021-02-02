def solution(sugar):
    answer=0
    while sugar>=0:
        if sugar%5==0:
            answer+=sugar//5
            print(answer)
            return
        sugar-=3
        answer+=1
    print(-1)

if __name__=="__main__":
    sugar=int(input())
    solution(sugar)