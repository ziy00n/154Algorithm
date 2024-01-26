# 백준 10799_쇠막대기
# 자료구조

import sys
input = sys.stdin.readline

bar = list(input().rstrip())
res = 0 # 잘린 조각 개수
rope = 0 # 쇠막대기 개수

for i in range(len(bar)):
    if bar[i] == ')':
        if bar[i-1] == ')':
            res += 1
            rope -= 1
        else: # 레이저()
            res += rope
    else: # ( 일 때
        if bar[i+1] != ')': # 다음 괄호가 )가 아니면(레이저가 아니면)
            rope += 1
print(res)