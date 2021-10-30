row_num, col_num = map(int,input().split())
spider_map: list=[]
for i in range(row_num):
    spider_map.append(input())
print(spider_map)
answer=[]
tmp_string= ""
for row_index in range(row_num):
    tmp_string:str=""
    for col_index in range(col_num):
        
        if spider_map[row_index][col_index]!="*":
            replace_num=0
            if col_index +1 < col_num and spider_map[row_index][col_index+1]=="*":
                replace_num+=1
            if col_index>=1 and spider_map[row_index][col_index-1]=="*":
                replace_num+=1
            if row_index+1 < row_num and spider_map[row_index+1][col_index]=="*":
                replace_num+=1
            if row_index>=1 and spider_map[row_index-1][col_index]=="*":
                replace_num+=1
            if row_index+1<row_num and col_index+1 < col_num and spider_map[row_index+1][col_index+1]=="*":
                replace_num+=1
            if col_index+1 < col_num and row_index>=1 and spider_map[row_index-1][col_index+1]=="*":
                replace_num+=1
            if row_index+1<row_num and col_index>=1 and spider_map[row_index+1][col_index-1]=="*":
                replace_num+=1
            if row_index >= 1 and col_index >= 1 and spider_map[row_index-1][col_index-1]=="*":
                replace_num+=1
            tmp_string+=(str(replace_num))
        else:
            tmp_string+="*"
            #spider_map[row_index][col_index]=str(replace_num)
    print(tmp_string)
    answer.append(tmp_string)
print(answer)