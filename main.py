array = list(map(float,input().split()))
array.sort(reverse=True)
a = array[0]
b = array[1]
c = array[2]
if a >= b + c:
    print('NAO FORMA TRIANGULO')
if a**2 == b**2+c**2:
    print('TRIANGULO RETANGULO')
if a**2 > b**2 + c**2:
    print('TRIANGULO OBTUSANGULO')
if a**2 < b**2 + c**2:
    print('TRIANGULO ACUTANGULO')
if a==b==c:
    print('TRIANGULO EQUILATERO')
if (a==b!=c) or (a!=b==c) or (b==a!=c):
    print('TRIANGULO ISOSCELES')