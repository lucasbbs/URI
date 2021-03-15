a, b = map(int, input().split())
if abs(a) % abs(b) == 0 or abs(b) % abs(a)==0:
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')