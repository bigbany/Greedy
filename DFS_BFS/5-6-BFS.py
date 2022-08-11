# BFS
# 너비 우선 탐색

from collections import deque

def bfs(graph, start, visited):
  queue= deque([start])
  visited[start]= True
  while queue:
    # queue 가 빌 때까지 반복
    v= queue.popleft()
    print(v, end =' ')
    # 왼쪽에서 제거하고 
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]= True
        print(visited, end ='\n')




graph= [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False]*9

bfs(graph,1,visited)