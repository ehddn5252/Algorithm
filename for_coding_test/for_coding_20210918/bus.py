

def solution(n, t, m, timetable):
    # 시간을 분단위로 변경 예) 10:00 => 600
    timetable = [int(time[:2]) * 60 + int(time[3:5]) for time in timetable]
    timetable.sort()  # timetable을 정렬
    last_time = (60 * 9) + (n - 1) * t  # 마지막 배차의 시간표 (분단위)

    for i in range(n):  # 배차 횟수만큼 반복
        if len(timetable) < m:  # timetable의 길이가 태울 수 있는 인원보다 적으면
            return '%02d:%02d' % (last_time // 60, last_time % 60)
        
        if i == n - 1:  # 마지막 배차일 경우
            if timetable[0] <= last_time:  # timetable에 마지막 배차 때 우선순위가 높은 크루가 있다면
                last_time = timetable[m - 1] - 1  # 마지막 탑승자보다 1초 빠르게 한다
            return '%02d:%02d' % (last_time // 60, last_time % 60)
        
        for j in range(m - 1, -1, -1):  # del로 인한 index 변화에 영향을 주지 않기위해서 거꾸로 반복 
            bus_arrive = (60 * 9) + i * t  # 다음 배차 시간 (분단위) 
            if timetable[j] <= bus_arrive:  # 다음 배차시간보다 작거나 같은 시간을 가진 timetable 요소를 삭제
                del timetable[j]  # timetable에서 다음 배차를 못하는 크루를 삭제
