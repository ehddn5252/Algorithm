#  Palindrome.. 완탐이네

def isPalindrome(x):
    if x==x[::-1]:
        return True

def solution(s):
    MAX=0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if isPalindrome(s[i:j]):
                if MAX < len(s[i:j]):
                    MAX = len(s[i:j])
    return MAX

'''
모든 문자열을 확인하는 문장이다. 
1. 팰린드롬인지 확인한다. 
2. 
'''