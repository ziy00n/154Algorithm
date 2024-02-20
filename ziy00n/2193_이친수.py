# 백준 2193_이친수
# DP
# --> *dp 2차원 배열로도 풀어보기*

import sys
input = sys.stdin.readline
n = int(input())

#dp[1] = 1: n이 1 일 때 이친수 갯수 1개(1)
dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])