

if __name__=="__main__":
    maps = ["XY..", "YX..", "..YX", ".AXY","AAAA"]
    check_list = [ [False for i in range(len(maps[0]))] for j in range(len(maps))]
    check_list[0][1]=True
    check_list[1][1]=True
    check_list[0][2]=True
    print(check_list)
