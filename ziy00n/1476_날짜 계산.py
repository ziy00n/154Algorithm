# 백준 1476_날짜 계산
# 완전탐색

import sys
input = sys.stdin.readline

e,s,m = map(int, input().split())

se, ss, sm = 1, 1, 1
year = 1

while True:
    if e == se and s == ss and sm == m:
        break
    se += 1
    ss += 1
    sm += 1
    year += 1

    if se > 15:
        se = 1
    if ss > 28:
        ss = 1
    if sm > 19:
        sm = 1

print(year)      