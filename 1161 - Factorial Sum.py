def calcFatorial(a):
  if a ==0:
    return 1
  total = 1
  counter = a
  for i in range(a):
    total *= counter
    counter -= 1
  return total

def read():
    try:
       return map(int, input().split())
    except EOFError:
        return None,None
while True:
  x, y = read()
  if x == None and y == None:
    break
  print(calcFatorial(x)+calcFatorial(y))