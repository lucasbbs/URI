a, b, c = map(float, input().split())
if b**2-4*a*c<0 or a == 0:
    print('Impossivel calcular')
else:
    print(f'R1 = {(-b + (b**2-4*a*c)**(1/2))/(2*a):.5f}')
    print(f'R2 = {(-b - (b**2-4*a*c)**(1/2))/(2*a):.5f}')