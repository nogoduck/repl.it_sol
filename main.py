#Boj 3184, sheep
from collections import deque
dx=  [-1,1,0,0]
dy = [0,0,-1,1]
#맵 확인
def printMap(map):
  for i in map:
    print(*i)
  print()

def bfs(fx, fy):
  global n, m
  q = deque([fx, fy])

  while q:
    a, b = q.popleft()
    for i in range(4):
      x = a + dx[i]
      y = b + dy[i]
      if 0 <= x < n and 0 <= y < m:
        if map

  while q

#맵 입력
n, m = map(int, input().split())

garden = [list(map(str, input().split()))for _ in range(n)]

check_garden = [[0] * m for _ in range(n)]


for i in range(n):
  for j in range(m):
    
printMap(garden)

printMap(check_garden)