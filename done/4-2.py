## 시각 
## 정수 N이 입력되면 00시00분00초부터 N시59분59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램 작성

N= int(input())

## 하루는 총 3600*24= 86400초 
## 시간, 분, 초 를 range로 넣는다  

count =0
for i in range(N+1):
  for m in range(60):
    for s in range(60):
      if '3' in str(i)+str(m)+str(s):
        count+=1 
print(count)