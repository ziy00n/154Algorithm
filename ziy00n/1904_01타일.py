# 백준 1904_01타일
# DP

import sys
input = sys.stdin.readline

N = int(input())

# dp = [0]*(N+1)
dp = [0] * 1000001 # indexError 방지
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746 # n이 1,000,000 이므로 연산 중간마다 15746을 나눠줘야 int범위 벗어나지 않음

print(dp[N])