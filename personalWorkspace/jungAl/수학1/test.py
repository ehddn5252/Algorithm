import sys

def get_gcd(a,b):
    gcd = 1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd

def get_lcm(a,b):
    gcd = get_gcd(a,b)
    lmc = a*b//gcd
    return lmc

s = int(sys.stdin.readline())

nums = list(map(int,sys.stdin.readline().strip().split(" ")))
lcm = nums[0]
first = nums[0]
for i in range(1,len(nums)):
    first = get_gcd(first,nums[i])
    lcm = get_lcm(lcm,nums[i])

print(f"{first} {lcm}")
# 최소 공배수는?