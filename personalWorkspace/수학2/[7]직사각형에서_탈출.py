

if __name__=="__main__":
    x,y,w,h=map(int,input().split())
    print(min(w-x,h-y,x,y))
