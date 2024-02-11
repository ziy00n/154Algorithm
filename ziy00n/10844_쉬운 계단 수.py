# 백준 10844_쉬운 계단 수
# DP

import sys
input = sys.stdin.readline

N = int(input())

dp = [[0] * 10 for _ in range(N + 1)] # dp 테이블

for i in range(1, 10): # 1의 자릿수의 경우의 수 초기화
    dp[1][i] = 1

# 나머지 자릿수의 경우의 수 탐색
for i in range(2, N + 1):
    for j in range(10):
        #가장 뒤에 오는 숫자 0이면, 그 앞엔 1만 가능
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        
        # 가장 뒤에 오는 숫자 1~8이면, 그 앞엔 +-1 가능
        elif j == 9:
            dp[i][j] = dp[i - 1][8]

        # 가장 뒤에 오는 숫자 9이면, 그 앞엔 8만 가능
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N]) % 1000000000)