# 음료수 얼려 먹기
# 1. 입력을 받자
N,M = map(int, input().split())

# 2. 매트릭스를 입력받자 

graph = []
for i in range(N):
  graph.append(list(map(int,input())))


# 3. 아이스크림 개수 세기
def dfs(x,y):
  # 범위를 벗어날때 false
  # 만약 상하 좌우 할때 벗어날 수 있으니
  if x<= -1 or x>=N or y<= -1 or y>=M :
    return False

  if graph[x][y]==0:
    graph[x][y]=1
    # 재귀식으로 처리
    # 상하 좌우 다 소환한다.
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    # 만약 0 일경우 true를 반환
    # 출발지점에서만 true 를 반환한다.
    # 출발지 근처에 있는 0들은 이미 1로 바뀐 상태
    return True
    
  return False
     


result =0
for i in range(N):
  for j in range(M):
    if dfs(i,j) == True:
      # 출발지점에서만 True 이기 때문에 
      result+=1
      
      
    
  