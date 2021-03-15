n = int(input())
n2 = n
notas100 = n // 100
n = n - notas100*100
notas50 = n // 50
n = n - notas50*50
notas20 = n // 20
n = n - notas20*20
notas10 = n // 10
n = n - notas10*10
notas5 = n // 5
n = n - notas5*5
notas2 = n // 2
n = n - notas2*2
print(n2)
print(f'{notas100} nota(s) de R$ 100,00')
print(f'{notas50} nota(s) de R$ 50,00')
print(f'{notas20} nota(s) de R$ 20,00')
print(f'{notas10} nota(s) de R$ 10,00')
print(f'{notas5} nota(s) de R$ 5,00')
print(f'{notas2} nota(s) de R$ 2,00')
print(f'{n} nota(s) de R$ 1,00')