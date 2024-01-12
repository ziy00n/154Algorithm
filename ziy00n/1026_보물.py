# 백준 1026_보물
# 그리디

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort() # 오름차순 정렬
result = 0

for num in A:
    max_b = max(B)
    B.pop(B.index(max_b)) # B 재배열 X, B의 최댓값을 불러와서 삭제 
    result += num * max_b # S의 최소값 = A배열에서 가장 작은 값 X B배열의 가장 큰 값

print(result)