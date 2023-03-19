n = input()
nums = ""
check_ans = [0]
for i in range(1, 30000):
    nums += str(i)
    check_ans.append(len(str(i)))
pointer = 0
ans=1
for num, i in enumerate(nums):
    if pointer == len(n):
        ans = num
        break
    if n[pointer] == i:
        pointer += 1
stacked = 0
for i in range(1, len(check_ans)):
    stacked += check_ans[i]
    if ans<=stacked:
        print(i)
        break
