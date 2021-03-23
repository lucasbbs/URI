numbers = list(map(int, input().split()))
sum = 0 
i = 1
N = 0
while N <= 0:
  N = numbers[i]
  i += 1
for n in range(numbers[0], numbers[0]+N):
  sum += n
print(sum)
