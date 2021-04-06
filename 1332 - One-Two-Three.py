def is_one(number):
  one = ['o', 'n', 'e']
  return [i == j for i, j in zip(one, number)].count(False) <= 1
def is_two(number):
  two = ['t', 'w', 'o']
  return [i == j for i, j in zip(two, number)].count(False) <= 1
def is_three(number):
  three = ['t', 'h', 'r', 'e', 'e']
  return [i == j for i, j in zip(three, number)].count(False) <= 1
N  = int(input())
for n in range(N):
  number = list(input())
  if is_one(number): print(1)
  elif is_two(number): print(2)
  elif is_three(number): print(3)
