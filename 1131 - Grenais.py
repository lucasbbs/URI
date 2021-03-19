grenais = []
while True:
  inter, gremio = map(int, input().split())
  grenais.append('inter' if inter > gremio else 'gremio' if inter < gremio else 'draw' )
  # print(grenais )
  # while True:
  new = int(input('Novo grenal (1-sim 2-nao)\n'))
    # if new == 2 or new == 1: break
  if new != 1: break
print(f'{len(grenais)} grenais')
inter = len([time for time in grenais if time == "inter"])
print(f'Inter:{inter}')
gremio = len([time for time in grenais if time == "gremio"])
print(f'Gremio:{gremio}')
draw = len([time for time in grenais if time == "draw"])
print(f'Empates:{draw}')
print( 'Inter venceu mais' if inter > gremio else 'Gremio venceu mais' if inter < gremio else 'Não houve vencedor' )
