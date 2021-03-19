N = int(input())
for i in range(N):
  x, y = map(int, input().split())
  print('divisao impossivel') if y==0 else print(f'{x/y:.1f}')