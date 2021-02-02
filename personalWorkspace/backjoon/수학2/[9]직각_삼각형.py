import time
import math



if __name__=="__main__":
    while True:
        numbers=list(map(int,input().split()))
        if numbers[0]==numbers[1]and numbers[1]==numbers[2] and numbers[1]==0:
            break
        numbers.sort()
        if numbers[2]**2==numbers[0]**2+numbers[1]**2:
            print("right")
        else:
            print("wrong")