# 백준 2003_수들의 합 2
# 투포인터

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1 # nums 배열의 인덱스
cnt = 0
sum = nums[0]

while (left <= right and right <= n):
    if sum < m: # 구간합이 M보다 작은 경우
        if right < n:
            sum += nums[right]
            right += 1
        else:
            break
    elif sum == m: # 구간합이 M과 같은 경우
        cnt += 1
        sum -= nums[left]
        left += 1
    else: # 구간합이 M보다 큰 경우
        sum -= nums[left]
        left += 1

print(cnt)