# 백준 5585_거스름돈
# 그리디

import sys
input = sys.stdin.readline

money = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in coins:
    if money >= coin:
        cnt += money // coin
        money %= coin
print(cnt)