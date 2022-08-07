## 왕실의 나이트
## 8x8 에서 수평*2 수직*1
## 수직*2 수평*1
## 2가지 방법으로 이동할 수 있다.
## 좌표를 입력하고 해당 좌표에서 이동할 수 있는 경우의 수를 출력하시오

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
## ord 를 통해 유니코드 정수를 반환한다.
## 유니코드 빼기  +1

result = 0
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2),
         (-2, 1)]
## 총 8가지 경우의 수가 있다.

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        ## row, column이 1과8 사이에 있을때만 result를 업데이트
        result += 1

print(result)
