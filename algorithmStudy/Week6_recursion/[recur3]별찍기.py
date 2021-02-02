# 작성 일자 : 20201204
# 작성자 : 김동우
# 문제명 : 2447 별 찍기 -10
# 문제 요약 : 

# 문제풀이 : 
# 1. 재귀적인 패턴으로 별을 찍는다 N이 3의 거듭제곱이다.
# N이 3보다 클 경우 N의 패턴은 공백으로 채워진 가운데의 (N/3) * (N/3)정사각형을 N/3의 패턴으로 둘러싼 형태이다 

# 다른 사람 코드
n = int(input())
pic = ['*'] * n * n
st_num = n

def star_write(n):
  for i in range(st_num):
    for j in range(st_num):
      if i%n >= n/3 and i%n < 2*n/3 and j%n >= n/3 and j%n < 2*n/3:
        pic[j+i*st_num] = ' '
  if n != 3:
    star_write(int(n/3))
  else:
    for i in range(st_num):
      for j in range(st_num):
        print(pic[j+i*st_num], end='')
      print()

star_write(n)

