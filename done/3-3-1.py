## 숫자카드 게임 
## 여러개의 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다. 
## N*M 형태로 카드가 놓여있다. 
## 한 행을 선택하고 
## 그 행에서 가장 작은 숫자의 카드를 뽑아야한다.

n,m = map(int, input().split())

result = 0 

for i in range(n):
  data= list(map(int, input().split()))

  min_value = min(data)
  
  result = max(result, min_value)
    ## min을 사용하여 list에서 최소값을 뽑아내고 
    ## max 비교를 통해 큰 값을 result 로 업데이트한다. 
  
print(result)