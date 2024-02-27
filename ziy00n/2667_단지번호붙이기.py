# 백준 2667_단지번호붙이기
# 그래프 BFS

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 상하좌우로 한 칸 씩 이동할 좌표
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = []

def bfs(graph, a, b):
    queue = deque()
    queue.append([a, b])
    graph[a][b] = 0
    count = 1
    
    while queue:
        x, y = queue.popleft()  # 큐의 좌표 x,y를 pop
        graph[x][y] = 0
        for i in range(4):  # 각 좌표마다 위 아래 왼쪽 오른쪽으로 이동
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue

            if graph[nx][ny] == 1:  # 집 방문 X 이면
                graph[nx][ny] = 0
                queue.append([nx, ny])  # 새로운 x ,y 좌표를 큐에 추가
                count += 1

    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: # 그래프의 원소가 1일때 bfs로 집 방문
            count = bfs(graph, i, j) 
            result.append(count)

result.sort()

print(len(result))  # 총 단지 수
for k in result:  # 각 단지마다 집의 수
    print(k)