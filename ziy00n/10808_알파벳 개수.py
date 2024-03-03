# 백준 10808_알파벳 개수
# 문자열

import sys
input = sys.stdin.readline

s = input().rstrip()
lst = [0]*26

for i in s:
    lst[ord(i)-97] += 1

for i in lst:
    print(i,end= ' ')