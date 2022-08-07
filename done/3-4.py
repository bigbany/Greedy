## 1이 될때까지

## N,K 를 입력받는다.

## (1)N에서 1을 빼거나 
## (2)N을 K로 나누거나  (나눠 떨어져야함.)

## 최소한의 연산으로 N을 1로 만드는 회수는? 

N,K = map(int,input().split())

count=0
while True:
  if(N%K==0):
    N/=K
    count+=1
  else:
    N-=1
    count+=1

  if(N==1):
    break

print(count)