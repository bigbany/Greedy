## 큰 수의 법치
## N 개의 자연수를
## 총 M회를 더한다. 
## 연속 K번까지 중복을 허용한다. 

## 입력예시
## 5 8 3
## 2 4 5 4 6 
## 6+6+6+5+6+6+6+5 
## 합은 46 

## 코드 시작

## 3개의 N,M,K 를 입력받고
## N 크기의 list를 입력 받아야한다. 

n,m,k = map(int , input().split())
## 여러 숫자를 받을 때 
## map(int, input().split())
## split 은 띄어쓰기 단위로 
print(n)
print(m)
print(k)
print('리스트를 입력하세요 ')
data = list(map(int, input().split()))
## 리스트 입력 받기
## map을 사용하고 list() 로 감싼다. 


data.sort()
first = data[n-1]
## 먼저 제일 큰, 그 다음 큰 수만 사용
second = data[n-2]

result =0 
## 결과 저장용 result 
while True:
## while True 로 그냥 시작
  
  for i in range(k):
    ## 연속 횟수 만큼 연산 시작
    if m==0:
    ## m 은 토탈 연산 횟수  
      break
      
    result += first
    m-=1
  if m==0:
    break
  result += second
  m-=1

print(result)
      