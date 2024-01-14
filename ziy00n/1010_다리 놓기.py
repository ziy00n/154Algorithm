# 백준 1010_다리 놓기
# DP

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1: # 서쪽 사이트 1개이면 동쪽 사이트 갯수만큼 다리 짓기 가능 
                dp[i][j] = j
            
            elif i == j: # 서쪽 사이트 갯수 = 동쪽 사이트 갯수면 다리 1개 짓기 가능
                dp[i][j] = 1
            
            else:
                if j > i: #서쪽 사이트 i, 동쪽 사이트 j개일 때 점화식
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    print(dp[n][m])