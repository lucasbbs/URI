notas = []
while True:
  nota = float(input()) 
  print('nota invalida')if not 0 <= nota <= 10 else notas.append(nota)
  if len(notas) == 2: 
    print(f'media = {sum(notas)/2:.2f}')
    new = None
    while new != 2 or new != 1:
      print('novo calculo (1-sim 2-nao)')
      new = int(input())
      if new == 2 or new == 1: break
    if new == 2: break
    notas = []
