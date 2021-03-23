numbers = []
while True:
  n = int(input())
  if n != 0: numbers.append(n)
  else: break
for n in range(len(numbers)):
  for m in range(1,numbers[n]+1):
    print(m, end = " ") if m != numbers[n] else print(m)