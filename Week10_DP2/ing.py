
# 안되노 ;;
def solution(str1,str2):
    maxSame=0
    for str1Index,str1String in enumerate(str1):
        for str2Index,str2String in enumerate(str2):
            if str1String == str2String:
                same=0
                i=0
                j=0
                print("===")
                while True:
                    if str1Index+i>=len(str1) or str2Index+j>=len(str2):
                        break

                    if str1[str1Index+i]==str2[str2Index+j]:
                        print(str1[str1Index+i])
                        same+=1
                        i+=1
                        j+=1
                        continue
                    elif str1[str1Index+i]!=str2[str2Index+j]:
                        
                        continue
                    elif str2Index+j==len(str2)-1:
                        i+=1
                        continue
                    

                if same>maxSame:
                    maxSame=same
    print(maxSame)



if __name__=="__main__":
    str1=input()
    str2=input()
    solution(str1,str2)