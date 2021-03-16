salary = float(input())

from bisect import bisect

rates = [0, 8, 18, 28]   # 10%  20%  30%

brackets = [2000,       
            3000,       
            4500]       

base_tax = [0,          # 2000 * 0%
            80,        # 1000 * 8%
            350]      # 1500 * 18% + 80

def tax(income):
    i = bisect(brackets, income)
    if not i:
        return 0
    rate = rates[i]
    bracket = brackets[i-1]
    income_in_bracket = income - bracket
    tax_in_bracket = income_in_bracket * rate / 100
    total_tax = base_tax[i-1] + tax_in_bracket
    return total_tax
if salary <= 2000:
  print('Isento')
else:
  print (f'R$ {tax(salary):.2f}')