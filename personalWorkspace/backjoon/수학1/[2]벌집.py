if __name__=="__main__":
    N=int(input())
    # 1 6 12 18 24 
    # 1 2~7 8~19 20 ~ 37 38~ 61
    if N==1:
        print(1)
        exit()
    start=1
    answer=1
    while start<N:
        start+=6*answer
        answer+=1
    print(answer)
