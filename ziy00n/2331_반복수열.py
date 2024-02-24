# 백준 2331_반복수열
# 수학

import sys
input = sys.stdin.readline

A, P = map(int, input().split())

check = [A]

while True:
    new = 0
    for i in (str(check[-1])):
        new += int(i) ** P
    if new in check:
        while True:
            if new == check.pop():
                print(len(check))
                exit()
    else:
        check.append(new)