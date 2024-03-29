# 백준 9095_1,2,3더하기
# DP

import sys
input = sys.stdin.readline

T = int(input()) 

for i in range(T):
    n = int(input())
    dp = [0]*12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    if n > 3:
        for i in range(4,n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    
    print(dp[n])