# 백준 1850_최대공약수
# 수학 / 유클리드 호제법


# 두 자연수 a,b에 대하여 a를 b로 나눈 나머지 r에 대해 a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 
# 이를 계속 반복하며 b가 0이 될 때, a값이 최대공약수

import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    else :
        return gcd(b, a % b) # (1071, 1029) = (1029, 42) = (42, 21) = (21, 0) = 21

A, B = map(int,input().split())

print(gcd(A, B) * "1")