n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
Array = n1,n2,n3,n4,n5
print(f'{len([n for n in Array if n % 2 ==0])} valores pares')