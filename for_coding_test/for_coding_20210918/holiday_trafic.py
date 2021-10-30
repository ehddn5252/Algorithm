'''
시스템 장애가 없는 명절을 보내고 싶다. 9월 15일 로그 데이터를 분석한 후 초당 최대 처리량으 계산해보기로 한다.
초당 최대 처리량은 요청의 응답 완료 여부와 관계없이 
***임의 시간부터 1초(=1,000밀리초)간 처리하는 요청의 최대 개수***
를 구하시오

그럼 24 * 60 * 60 = 24 * 3,600 = 144 * 6 * 100 = 86,400 초
소수 3째자리까지 포함이므로 86,400,000 milli second
리스트의 크기는 86,400,000

방법으로는 시간을 milli second 단위로 만들어서 입력 값을 리스트에 넣어준다. 
그 다음 그 구간인 값을 1씩 올리는 방법, 그 후 max(list)를 사용한다.
'''

import re
def time_converter(num:int,type:str):
    if type == "HOUR":
        num = num*60*60*1000
    elif type =="MINUATE":
        num = num *60*1000
    elif type =="SECOND":
        num = num * 1000
    else:
        pass

    return num

def solution(lines):
    answer = 0
    answer_list=[]
    for line in lines:
        pattern = "(\d{2}):(\d{2}):(\d{2}).(\d{3}) (\d).?(\d*)s"
        string = line
        a = re.findall(pattern,string)
        time = a[0]
        print(time)
        end_second = time_converter(num=int(time[0]),type="HOUR")+time_converter(int(time[1]),type="MINUATE")+time_converter(int(time[2]),type="SECOND")+time_converter(int(time[3]),type="MILLISECOND")
        print((int(time[4])*1000 + int(time[5].ljust(3,'0'))))
        start_second = end_second - (int(time[4])*1000 + int(time[5].ljust(3,'0'))) +1
        answer_list.append((start_second, end_second))

    for i in range(len(lines)):
        end_1s = answer_list[i][1] +1000 -1
        cnt = 1
        for j in range(i+1,len(lines)):
            if answer_list[j][0]<= end_1s:
                cnt+=1
        answer = max(answer,cnt)
    return int(answer)

if __name__=="__main__":

    lines = ["2016-09-15 01:00:04.002 2.0s","2016-09-15 01:00:07.000 2s"]
    lines = ["2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"]
    solution(lines)