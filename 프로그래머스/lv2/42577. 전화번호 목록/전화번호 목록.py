def solution(phone_book):
    phone_book.sort()
    dict1 = {}
    for i,v in enumerate(phone_book):
        if i== len(phone_book)-1:
            break
        # if phone_book[i+1].startswith(v):
        #     return False
        if phone_book[i+1][:len(v)]==phone_book[i]:
            return False
            
    return True