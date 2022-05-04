def hanoi(to_move_disk_num,f,t,v):
    if to_move_disk_num==1:
        print(f+"->"+ t)

    else:
        hanoi(to_move_disk_num-1,f,v,t)
        print(f +"->" + t)
        hanoi(to_move_disk_num-1,v,t,f)

hanoi(3,'a','b','c')