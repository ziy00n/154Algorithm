# 백준 7576_토마토
# BFS

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split()) # N:행, M:열

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([])

for i in range(N): # 행
    for j in range(M): # 열
        if graph[i][j] == 1: # 익은 토마토의 좌표
            queue.append([i, j]) # 큐에 삽입

def bfs():
    while queue:
        x, y = queue.popleft() # 익은 토마토의

        for i in range(4):  # 상하좌우 돌면서
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0: # 안익은 토마토면(0) (토마토 없는 곳(-1)은 넘어감)
                    graph[nx][ny] = graph[x][y] + 1 # 익힌 후(1)
                    queue.append([nx, ny]) # 큐에 넣기 
bfs()

ans = 0
for line in graph:
    for tomato in line:
        if tomato == 0:
            # 안익은 토마토(0)이 있으면 바로 정지
            print(-1)
            exit()
    ans = max(ans, max(line))

print(ans-1) # 1에서 시작했기 때문에 결과 값 - 1