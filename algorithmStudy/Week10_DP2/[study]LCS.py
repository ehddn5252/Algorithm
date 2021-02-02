
# DP 알고리즘 떠올리기가 너무 어렵다.. 


def solution(str1,str2):
    str1Len=len(str1)
    str2Len=len(str2)

    dp=[[0]*(str2Len+1)  for _ in range(str1Len+1)]
    for i in range(1,str1Len+1):
        for j in range(1,str2Len+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print(dp)
    for i in range(len(dp[0])):
        print(dp[i])
    #print(dp[-1][-1])


if __name__=="__main__":
    str1="ACAYKP"#input()
    str2="CAPCAK"#input()
    solution(str1,str2)



'''
#파이썬 1등
def s():
    s1, s2 = input(), input()
    dp = [0] * 1000
    # 문자열 1
    for i in range(len(s1)):
        max_dp = 0
        #문자열2 
        for j in range(len(s2)):
            if max_dp < dp[j]:
                max_dp = dp[j]
            # 
            elif s1[i] == s2[j]:
                dp[j] = max_dp + 1
    print(max(dp))
s()
'''
'''
 C++ 2등
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string.h>

using namespace std;

typedef pair<int, int> pi;

int main()
{
	int dp[2][1003] = { 0, }, idx = 0, i, j;
	char a[1003], b[1003];
	scanf("%s %s", a + 1, b + 1);

	for (i = 1; a[i]; i++) {
		for (j = 1; b[j]; j++) {
			if (a[i] == b[j]) dp[idx][j] = dp[idx ^ 1][j - 1] + 1;
			else dp[idx][j] = max(dp[idx][j - 1], dp[idx ^ 1][j]);
		}
		idx ^= 1;
	}

	printf("%d", dp[idx ^ 1][j - 1]);
	return 0;
	
}

'''