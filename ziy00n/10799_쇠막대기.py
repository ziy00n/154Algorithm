# 백준 10799_쇠막대기
# 자료구조

import sys
input = sys.stdin.readline

ib = input().rstrip()
stack = []
cnt = 0
for i in range(len(ib)):
    if ib[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if ib[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)