# 백준 11724_연결 요소의 개수
# 그래프 - DFS

import sys
# 재귀 제한
sys.setrecursionlimit(10**7) # 지정안하면 재귀 호출 시 런타임 에러
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

count = 0
for i in range(1, n+1):
    if visited[i] == False:
        count += 1
        dfs(i)
        
print(count)