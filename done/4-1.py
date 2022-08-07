## 상하좌우 문제
## N을 입력받는다.
## 처음은 1,1 에서 시작 
## R,L,U,D 
## NxN 을 벗어나는 이동은 무시
## 최종 목적 좌표를 구하시오 

N = int(input())
x,y =1,1 

plans = input().split()

## plans는 list 로 받는다.

move_types = ['L','R','U','D']
dx = [0,0,-1,1]
dy= [-1,1,0,0]

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x+ dx[i]
      ny = y+ dy[i]
  if nx<1 or ny<1 or nx> N or ny> N:
      continue
    # nx ,ny 가 이상하면 x,y를 업데이트 시키지 않는다. 
  x,y = nx, ny

print(x,y)