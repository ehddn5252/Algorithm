'''
자카드 유사도 : 집한간의 유사도를 검사하는 방법 중 하나.
두 집합의 교집합의 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.

문자는 두 글자씩 끊어서 다중 집합의 원소로 만들고 공백이나 특수문자가 있는 경우 그 글자 쌍을 버린다.

'''
import copy

def jaccard_similarity(str1,str2,slice_size):
    # slice_size = 2
    str1_slice:list=[]
    str2_slice:list=[]
    str1_slice.append(str1[-slice_size:])
    str2_slice.append(str2[-slice_size:])
    
    for i in range(len(str1)):
        if len(str1)==i+slice_size:
            break
        word = str1[i:i+slice_size]
        if word.isalpha():
            str1_slice.append(str1[i:i+slice_size])
    
    for i in range(len(str2)):
        if len(str2)==i+slice_size:
            break
        word = str2[i:i+slice_size]
        if word.isalpha():
            str2_slice.append(str2[i:i+slice_size])

    # 교집합과 합집합 찾아야 한다. 이는 해쉬로 설정하자.
    str1_hash = {}
    str2_hash = {}

    for i in str1_slice:
        str1_hash[i] = str1_hash.get(i,0)
        str1_hash[i]+=1
    
    for i in str2_slice:
        str2_hash[i] = str2_hash.get(i,0)
        str2_hash[i]+=1
    
    inner_join=0
    outer_join=0
    str_slice=[]
    for i in range(len(str1_slice)):
        str_slice.append(str1_slice[i])
    
    for i in range(len(str2_slice)):
        str_slice.append(str2_slice[i])
    
    str_slice = (list(set(str_slice)))
    
    print(str_slice)
    for i in str_slice:
        inner_join += min(str1_hash.get(i,0),str2_hash.get(i,0))
        outer_join += max(str1_hash.get(i,0),str2_hash.get(i,0))
    return inner_join / outer_join

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    answer = 0
    answer = int(jaccard_similarity(str1,str2,2) * 65536 )
    print(answer)
    return answer


if __name__=="__main__":
    testcase = [("FRANCE","french"),("handshake","shake hands"),("aa1+aa2","AAAA12"),("E=M*C^2","e=m*c^2")]
    testcase = [("aa1+aa2","AAAA12")]
    for str1,str2 in testcase:
        solution(str1,str2)


'''
def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if str2[i:i+2].isalpha()]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)
'''