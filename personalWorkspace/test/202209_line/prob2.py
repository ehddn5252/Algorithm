from typing import List
import re

def check_word(k,dic,word):
    pattern= ""
    replaced_word = ""
    for i in word:
        replaced_word+="#"
        if i=='.':
            # [a-z]{1,3} abc afx apq fpa
            pattern += '[a-z]{1,' + str(k) + '}'
        else:
            pattern+=i

    for slang in dic:
        m = re.fullmatch(pattern,slang)
        if m is not None:
            return replaced_word
    return word


def solution(k: int, dic: List[str], chat: str) -> str:

    answer = ''
    ans_list = []
    chat_list = chat.split(" ")

    for word in chat_list:
        new_word=check_word(k,dic,word)
        answer+=new_word+" "
    return answer.rstrip()

k = 2
dic = ["slang","badword"]
chat = "badword ab.cd bad.ord .word sl.. bad.word"

solution(k,dic,chat)