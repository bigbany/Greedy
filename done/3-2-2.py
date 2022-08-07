## 큰 수의 법치
## N 개의 자연수를
## 총 M회를 더한다. 
## 연속 K번까지 중복을 허용한다. 

## 좀 더 빠른 방식으로 풀기
## 총 연산 회수 M의 값이 크다면
## 시간 내에 못 풀 수도 있다.
## M 회를 더하는 연산이 아니라 
## 중복으로 더해지는 값을 찾고 곱해버리는 것이 메모리 절약에 좋다.

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

count=int(m/(k+1))*k
count += m%(k+1)
## count 는 제일 큰 수의 총 연산회수 

result += count*first
result += (m-count)*second
## 총 연산에서 큰 수의 연산 회수 count를 빼면 
## 두번째 큰 수의 연산 회수가 나온다

print(result)
      