array = list(map(float,input().split()))
array.sort(reverse=True)
a, b, c = array
if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
  if a**2 == b**2+c**2:
      print('TRIANGULO RETANGULO')
  if a**2 > b**2 + c**2:
      print('TRIANGULO OBTUSANGULO')
  if a**2 < b**2 + c**2:
      print('TRIANGULO ACUTANGULO')
  if a==b==c:
      print('TRIANGULO EQUILATERO')
  elif a == b or a == c or b == a or b == c or c == a or c ==b:
      print('TRIANGULO ISOSCELES')