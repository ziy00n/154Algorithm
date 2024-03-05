# 백준 24444_알고리즘 수업 - 너비 우선 탐색 1
# BFS (인접리스트)

from collections import deque
import sys
input = sys.stdin.readline

# 정점 수, 간선 수, 시작 정점
N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v) # 인접 리스트
    graph[v].append(u)

# 인접 노드 오름차순 정렬
for i in range(N+1):
    graph[i].sort()
    print(graph[i])

seq = 1
def bfs(graph, visited, R):
    global seq
    queue = deque([R]) # 시작 정점 R을 방문
    visited[R] = seq # 방문한 순서 저장

    while queue:
        v = queue.popleft()
        # graph[v].sort() # 인접 노드 오름차순 정렬
        print(graph[v])
        for i in graph[v]: # 인접 노드 중
            if visited[i] == 0: # 방문안했으면 큐에 추가
                queue.append(i)
                seq += 1
                visited[i] = seq # 방문 순서 저장

bfs(graph, visited, R)

#출력
for i in range(1, N+1):
    print(visited[i])