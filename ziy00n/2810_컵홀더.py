# 백준 2810_컵홀더
# 그리디

import sys
input = sys.stdin.readline

n = int(input())
seat = input()
couple = seat.count('LL') # 커플석 갯수

if couple <= 1:
    print(n)
else:
    print(n + 1 - couple)