



if __name__=="__main__":
    N=int(input())
    i=1
    times=0
    
    while(N>0):
        N-=i
        i+=1
        times+=1
    #짝수면 내려가는거
    if times%2==0:
        # 분자
        numerator=times+N 
        # 분모
        denominator=-N+1
    elif times%2==1:
        numerator=-N+1
        denominator=times+N 
    answer= str(numerator)+"/"+str(denominator)
    print(answer)
