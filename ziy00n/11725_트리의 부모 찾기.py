# 백준 11725 트리의 부모 찾기
# DFS - 인접리스트

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

N = int(input())  # 노드의 개수

graph = [[0] for _ in range(N+1)]
visited = [0] * (N+1) 

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b) # 인접리스트
    graph[b].append(a)

def dfs(v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)

dfs(1)

for i in range(2, N+1):
    print(visited[i])