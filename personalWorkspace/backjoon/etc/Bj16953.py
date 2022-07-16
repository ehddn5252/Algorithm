A, B = map(int, input().split(" "))

def multify(a):
    return a * 2

def add_one(a):
    ret = int(str(a) + "1")
    return ret

result = 99999
can_make = False

def f(num, times):
    global B, result, can_make
    if num > B: return
    if num == B and times < result:
        can_make = True
        result = times
        return
    f(multify(num), times + 1)
    f(add_one(num), times + 1)

f(A, 1)
print(result if can_make else -1)
