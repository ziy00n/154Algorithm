# 백준 24479_알고리즘 수업 - 깊이 우선 탐색 1
# DFS 
# 인접 리스트 방법 (인접 행렬X)

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6) # 재귀 깊이 제한 변경

# 정점 수, 간선 수, 시작 정점
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 인접리스트
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) 
    graph[b].append(a)
    

# 방문한 노드 (시작정점에서 방문할 수 없는 경우 0 출력)
visited = [0] * (N+1) 

seq = 1

def dfs(v):
    global seq
    visited[v] = seq # 시작 노드 방문처리
    graph[v].sort() # 오름차순
    for i in graph[v]:    
        if visited[i] == 0:
            seq += 1
            dfs(i)

dfs(R)

for i in range(1, N+1):
    print(visited[i]) #  i번째 줄에 정점 i의 방문 순서 출력