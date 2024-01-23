# 백준 2003_수들의 합 2
# 투포인터

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
cnt = 0

while (left <= right and right <= n):

    # 구간 합
    total = sum(nums[left:right]) #슬라이싱

    if total < m: # 구간 합이 M보다 작은 경우
        right += 1
    
    elif total > m: # 구간 합이 M보다 큰 경우
        left += 1
    else: # 구간 합이 M과 같은 경우
        cnt += 1
        right += 1 #left += 1도 가능 

print(cnt)