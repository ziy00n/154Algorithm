# 백준 1783_병든 나이트
# 그리디

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
result = 0

if n == 1:
    result = 1
elif n ==2 :
    result = min(4, (m+1)//2)
else:
    if m < 7:
        result = min(4, m)
    else:
        result = m-2

print(result)