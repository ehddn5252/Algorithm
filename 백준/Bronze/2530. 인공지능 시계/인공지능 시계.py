
h,m,s = map(int,input().split(" "))
input_s = int(input())

now = 3600*h + 60 *m + s + input_s

trans_now = now %(3600*24)
next_h = trans_now//3600
trans_now-= 3600*next_h
next_m = trans_now//60
trans_now-= 60*next_m
next_s = trans_now
print(f"{next_h} {next_m} {next_s}")