def fib(n):
    result = []
    i = 0
    a, b = 0, 1
    while i <= n:
        result.append(a)
        a, b = b, a+b
        i += 1
    return result

n =int(input())
i = 0
while True:
    number = int(input())
    print(f'fib({number}) = {fib(number+1)[-1]*2-2} calls = {fib(number)[-1]}')
    i +=1
    if i == n:
      break