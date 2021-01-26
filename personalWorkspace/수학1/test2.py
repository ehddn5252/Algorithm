# Fly me to the Alpha Centauri

def solution(distance):
    print("distacne : "+str(distance))
    
    if distance==1:
        print(1)
    elif distance==2:
        print(2)
    elif distance==3 or distance==4:
        print(3)
    else:
        chance=1
        i=2
        answer=3
        while distance-4>0:
            if chance%2==0:
                i+=1
            distance-=i
            chance+=1
            answer+=1
        print(answer)
        
if __name__=="__main__":
    
        solution(distance)