a,b,c = map(int, input().split())
def MaiorAB(a,b):
  return (a+b+abs(a-b))/2

if MaiorAB(a,b) == a:
  if MaiorAB(a,c) == a:
    print(f'{a} eh o maior')
  elif MaiorAB(b,c) == b:
    print(f'{b} eh o maior')
  else:
    print(f'{c} eh o maior')