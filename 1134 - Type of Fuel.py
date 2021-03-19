array = []
while True:
    m = int(input())
    if m == 1 or m ==2 or m ==3: array.append(m)
    if m == 4: break
def typeOfFuel(x):
    return {
        1: f'Alcool: {array.count(1)}',
        2: f'Gasolina: {array.count(2)}',
        3: f'Diesel: {array.count(3)}'
    }[x]
print('MUITO OBRIGADO')
for i in range(1,4):
  print(typeOfFuel(i))