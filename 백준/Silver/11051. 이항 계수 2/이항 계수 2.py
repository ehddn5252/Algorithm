n,k = map(int,input().split(" "))
def factorial(n):
  ans=1
  for i in range(1,n+1):
    ans*=i
  return ans

s = 0
formula = factorial(n)//(factorial(k)*factorial(n-k))%10007
print(formula)