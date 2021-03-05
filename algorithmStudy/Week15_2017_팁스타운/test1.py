str1 = "1234"

objStr="12345678"

if str1 in objStr:
    print("True")
    index=objStr.find(str1)
    objStr=objStr[:index]+objStr[index+len(str1):]
    print(f'objStr: {objStr}')
    print(f'len(objStr): {len(objStr)}')