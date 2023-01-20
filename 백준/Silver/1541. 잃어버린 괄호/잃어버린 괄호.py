formula = input()
new_formula = ""
num = ""
nums = []
operators = []
for index, i in enumerate(formula):
    if i == '+' or i == '-':
        operators.append(i)
        nums.append(int(num))
        num = ""
    else:
        num += i

    if index == len(formula) - 1:
        nums.append(int(num))

op_index = 0
ans = nums[0]
if len(nums) == 1:
    pass
elif len(nums) == 2:
    if operators[0] == '+':
        ans += nums[1]
    else:
        ans -= nums[1]
else:
    minus_flag = False
    while True:
        if op_index >= len(operators):
            break

        if operators[op_index] == '-':
            minus_flag = True
        if minus_flag:
            ans -= nums[op_index + 1]
        else:
            ans+=nums[op_index + 1]
        op_index+=1
print(ans)
