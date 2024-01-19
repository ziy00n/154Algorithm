# 백준 10162_전자레인지
# 그리디

import sys
input = sys.stdin.readline

seconds = [300, 60, 10]
result  = []

T = int(input())

# 3개 버튼으로 맞춰지지 않는 T초 = 3개 버튼 시간의 최대공약수로 나눠지지않음

if T % 10 != 0: # 최대공약수 = 10
    print(-1)
else:
    for s in seconds:
        result.append(T//s)
        T %= s
    print(result[0], result[1], result[2], sep= ' ')   