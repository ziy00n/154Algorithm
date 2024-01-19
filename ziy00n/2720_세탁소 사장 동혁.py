# 백준 2720_세탁소 사장 동혁
# 그리디

import sys
input = sys.stdin.readline

T = int(input())

coins = [25, 10, 5, 1] # 쿼터, 다임, 니켈, 페니

for _ in range(T):
    c = int(input())
    result = [] # 각 동전의 갯수(coins 리스트 순서대로)
    for i in coins:
        result.append(c//i) # 몫 = 해당 동전 갯수
        c %= i # 나머지 = 남은 거스름돈
    #print(' '.join(map(str, result)))
    print(*result)