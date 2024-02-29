# 백준 10451_순열 사이클
# DFS

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

T = int(input())

def dfs(v):
    visited[v] = True 
    nv = graph[v]
    if not visited[nv]:
        dfs(nv)

for _ in range(T):
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (N+1)
    result = 0
    
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            result += 1
    print(result)