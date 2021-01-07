answerList=[]
checkList=[]
def DFS(transFormedWord,check,words,target):
    global checkList
    if check>len(words):
        checkList=[]
        return
    if target==transFormedWord:
        answerList.append(check)
        checkList=[]  
        return

    for word in words:
        for i in range(len(word)):
            if transFormedWord.startswith(word[0:i]) and transFormedWord.endswith(word[i+1:]) and word not in checkList:
                checkList.append(word)
                DFS(word,check+1,words,target)
                break


def solution(begin, target, words):
    if target not in words:
        return 0
    DFS(begin,0,words,target)
    if not answerList:
        return 0
    print(min(answerList))
    return min(answerList)

