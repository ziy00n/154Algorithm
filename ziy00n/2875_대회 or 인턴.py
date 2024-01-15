# 백준 2875_대회 or 인턴
# 그리디

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

for i in range(k):
    if n//2 < m:
        m -= 1
    else:
        n -= 1

print(min(n//2, m))