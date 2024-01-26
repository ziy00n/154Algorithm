# 백준 10819_차이를 최대로
# 완전탐색

import sys, itertools
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
arr = itertools.permutations(A, n)
sum = []

for i in arr:
    s=0
    i_list = list(i)
    for j in range(1, n):
        s += abs(i_list[j]-i_list[j-1])
    sum.append(s)

print(max(sum))