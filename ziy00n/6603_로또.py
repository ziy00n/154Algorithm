# 백준 6603_로또
# 완전탐색
import sys
from itertools import combinations

input = sys.stdin.readline

while(True):
    S = list(map(int, input().split()))
    if S[0] == 0 and len(S) == 1:
        break
    else:
        for i in combinations(S[1:], 6):
            print(*i)
    print()