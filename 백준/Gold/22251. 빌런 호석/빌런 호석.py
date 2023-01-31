'''
1. 인풋정보 쓰기
2. 글 똑바로 읽기
3. 해결방안 모색
4. 의사코드 
5. 해결

'''


# 0~ 9 까지 LED 코드

def to_2(str1):
    return int(str1, 2)


def get_bin_all_cal(str1, str2):
    global transfer_map
    ret = 0
    for i in range(len(str1)):
        check = int(str1[i])
        check2 = int(str2[i])
        ret += transfer_map[check][check2]
    return ret


def get_bin_oper_calc(str1, str2):
    strings = bin(to_2(str1) ^ to_2(str2))
    return strings

def get_strs_1count(str1):
    count = 0
    for i in range(len(str1)):
        if str1[i] == '1':
            count += 1
    return count


if __name__ == "__main__":
    l = ["1111110", "0110000", "1101101", "1111001", "0110011", "1011011", "1011111", "1110000", "1111111", "1111011"]
    INF = 2147000000
    N, K, P, X = map(int, input().split(" "))  # 최대 N층, 디스플레이 K개, 최대 P개 반전, X 층에 멈춤
    transfer_map = [[INF for _ in range(10)] for _ in range(10)]
    for i in range(len(l)):
        for j in range(len(l)):
            transfer_map[i][j] = get_strs_1count(get_bin_oper_calc(l[i], l[j]))
    ans = 0
    for i in range(1, N+1):
        if i==X:
            continue
        tmp_x = str(i).rjust(K, '0')
        tmp_y = str(X).rjust(K, '0')
        test = get_bin_all_cal(tmp_x, tmp_y)
        if test <= P:
            ans += 1
    print(ans)
