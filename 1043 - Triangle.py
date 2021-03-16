array = list(map(float, input().split()))
array.sort(reverse=True)
a,b,c = array
if a < b + c:
  print(f'Perimetro = {a+b+c:.1f}')
else:
  print(f'Area = {(a+b)*c/2}')