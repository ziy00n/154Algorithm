# 백준 4796_캠핑
# 그리디

import sys
input = sys.stdin.readline

i = 1

while True:
    l, p, v = map(int, input().split())
    
    if p == 0 and l==0 and v==0: # 0 0 0 입력되면 종료
        break

    camping = (l * (v//p)) + min((v%p), l) # 캠핑장 사용가능한 최대 일수
    print('Case {}:'.format(i), camping)
    i += 1 