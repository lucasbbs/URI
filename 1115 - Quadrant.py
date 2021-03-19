def setQuadrant(x,y):
  (print('primeiro') if y > 0 else print('quarto')) if x > 0 else print('segundo') if y > 0 else print('terceiro')

while True:
  x, y = map(int, input().split())
  if x == 0 or y == 0: break
  else: setQuadrant(x,y)