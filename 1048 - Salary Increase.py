salary = float(input())
def readjustmentRate(salary):
    if 0 <= salary <= 400.00:
        return 0.15
    elif 400.01 <= salary <= 800.00:
        return 0.12
    elif 800.01 <= salary <= 1200.00:
        return 0.10
    elif 1200.01 <= salary <= 2000.00: 
        return 0.07
    elif salary > 2000.00:
        return 0.04

print(f'Novo Salario: {salary*(1+readjustmentRate(salary)):.2f}')
print(f'Reajuste ganho: {salary*readjustmentRate(salary):.2f}')
print(f'Em percentual: {readjustmentRate(salary)*100:.0f} %')