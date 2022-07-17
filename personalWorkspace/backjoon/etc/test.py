#
l = [2, 4, 7, 10, 20, 30, 50, 51, 53, 60, 80, 99, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100]
find_num = 53

start = 0
end = len(l)
while start <= end:
    middle = (start + end) // 2
    print(f'start:{start} end:{end}, middle:{middle}')
    # 선택한 값이 찾을 숫자보다 큰 경우
    if l[middle] > find_num:
        end = middle - 1
    elif l[middle] < find_num:
        start = middle + 1
    else:
        print(f"53 is l[{middle}]")
        break
