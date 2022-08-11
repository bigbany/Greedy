# 인접행렬 매트릭스로 표현
INF = 999999999

graph = [
  [0,7,5],
  [7,0,INF],
  [5,INF,0]  
]

print(graph)

# 인접 리스트 로 표현
GRAPH = [[]for _ in range(3)]

GRAPH[0].append((1,7))
GRAPH[0].append((2,5))
GRAPH[1].append((0,7))
GRAPH[2].append((0,5))

print(GRAPH)