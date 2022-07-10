
bracket_dict= {')':'(', ']':'['}
l=""
while True:
    tmp_l = input()
    l += tmp_l
    if l == ".":
        break
    elif l[-1]!=".":
        pass
    else:
        stack = []
        yes_flag = True
        for i in l:
            if i == '(' or i == '[':
                stack.append(i)
            elif i==')' or i==']':
                if stack!=[]:
                    popped = stack.pop()
                else:
                    print('no')
                    yes_flag = False
                    break

                if popped != bracket_dict[i]:
                    print('no')
                    yes_flag=False
                    break
        if yes_flag:
            if stack!=[]:
                print('no')
            else:
                print('yes')
        l=""