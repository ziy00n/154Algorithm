# 백준 1107_리모컨
# 브루트포스

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
start = 100

if M != 0:
    miss = list(map(int, sys.stdin.readline().split()))
else:
    miss = []
result = abs(N-start)

for i in range(1000000):
    for j in str(i):
        if int(j) in miss:
            break
    else:
        result = min(result, len(str(i))+abs(N-i))

print(result)