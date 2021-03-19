notas = []
while True:
  nota = float(input()) 
  print('nota invalida')if not 0 <= nota <= 10 else notas.append(nota)
  if len(notas) == 2: break
print(f'media = {sum(notas)/2:.2f}')