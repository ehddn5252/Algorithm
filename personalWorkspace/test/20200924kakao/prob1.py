
def convert_date_to_day(year,month,day):
    converted_day = year * 12 * 28 + month * 28 + day
    return converted_day

def solution(today, terms, privacies):
    answer = []
    terms_dict ={}
    for term in terms:
        term_list = term.split(" ")
        terms_dict[term_list[0]]=int(term_list[1])*28
    today_list = list(map(int,today.split(".")))
    today_day = convert_date_to_day(today_list[0],today_list[1],today_list[2])

    for i,privacy in enumerate(privacies):
        privacy_list = privacy.split(" ")
        privacy_date_list = list(map(int,privacy_list[0].split(".")))
        before_day = convert_date_to_day(privacy_date_list[0],privacy_date_list[1],privacy_date_list[2])
        if today_day>=before_day + terms_dict[privacy_list[1]]:
            answer.append(i+1)
    return answer


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

solution(today,terms,privacies)