# while True:
#   N = int(input())
#   slugs = []
#   try:
#     slugs = list(input().split())
#     if len([n for n in slugs if int(n) >= 20]) != 0:
#       print (3)
#     elif len([n for n in slugs if int(n) >= 10]) != 0:
#       print (2)
#     else:
#       print (1)
#   except EOFError:
#     break



while True:
    try:
      n = 0
      while n >= 0:
        n = int(input())
        soma = 0
        i = 0
        slugs = int(input().split())
        maior = 0
        for i in range(n):
          x = slugs[i]
          if x > maior: maior = x
          i += 1
        print(3) if maior >= 20 else( print(2) if maior >= 10 else print(1))
    except EOFError:
      break