# queue 예제

from collections import deque
## collections 로 부터 deque를 가져온다. 
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()
# 제거할때 popleft, popright 로 제거 가능하며
print(queue)
queue.reverse()
# reverse를 통해서 가능함 .
print(queue)