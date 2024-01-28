# 백준 1697_숨바꼭질
# BFS

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

d = [0]*100001

def bfs(n):
    queue = deque()
    queue.append(n)
    while queue:
        v = queue.popleft()
        if v == k:
            print(d[v])
            break

        for next in (v-1, v+1, v*2):
            if 0 <= next < 100001 and not d[next]:
                d[next] = d[v] + 1
                queue.append(next)

bfs(n)