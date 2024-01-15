# 백준 10610_30
# 그리디

import sys
input = sys.stdin.readline

num = input().rstrip()
num_lst = list(num)
num_lst.sort(reverse=True) # 내림차순 정렬

# 30의 배수 특징
# 1. 3의 배수 > 모든 자릿수의 합이 3의 배수
# 2. 10의 배수 > 자릿수에 0이 포함되어야함

if num_lst[-1] != '0': # 30의 배수이므로 숫자 내 0이 없다면 -1
    print(-1)

else :
    sum = 0
    for i in num_lst:
        sum += int(i) # 자릿수의 합
    if sum % 3 != 0: # 자릿수의 합이 3의 배수가 아니면 -1
        print(-1)
    else :
        print(''.join(num_lst))