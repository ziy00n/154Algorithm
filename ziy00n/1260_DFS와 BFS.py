# 백준 1260_DFS와 BFS
# 그래프 DFS/BFS
# DFS:재귀, BFS:deque 사용

from collections import deque
import sys
input = sys.stdin.readline

# n:정점의 개수, m:간선의 개수, v: 탐색 시작 정점 번호
n, m, v = map(int, input().split())
graph =[[False] * (n+1) for _ in range(n+1)]

# 간선으로 연결된 정점에 1 입력
for _ in range(m) :
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

# 방문여부
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def dfs(v):
    visited_dfs[v] = True
    print (v, end=" ")

    for i in range(1, n+1):
        if not visited_dfs[i] and graph[v][i] == 1: #i값 방문안하고 v와 연결되어있다면
            dfs(i) # i값으로 dfs를 돌며 깊이우선탐색

def bfs(v):
    #방문할 곳을 순서대로 넣을 큐
    queue = deque([v])
    #방문 처리
    visited_bfs[v] = True
     # 큐가 다 빌 때까지 돌기
    while queue:
    #큐 맨 앞에 있는 값을 꺼내서 출력
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, n + 1): # 1부터 n까지 돌기
         # i값의 방문기록이 없고, v와 연결되어있다면
            if not visited_bfs[i] and graph[v][i] == 1:
                queue.append(i) #큐에 추가한다.
                visited_bfs[i] = True

dfs(v)
print()
bfs(v)