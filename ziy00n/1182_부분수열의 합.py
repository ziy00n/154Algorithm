# 백준 1182_부분수열의 합
# 완전탐색

import sys, itertools
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
res = 0

for i in range(1, n+1):
    for l in itertools.combinations(arr,i):
        if (sum(l) == s):
            res += 1;
print(res)