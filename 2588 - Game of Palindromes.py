while True:
   try:
      entrada = input()
   except EOFError:
      break

   letras_unicas = set([i for i in set(list(entrada)) if entrada.count(i) %2 != 0])

   if len(letras_unicas) > 1:
      print(len(letras_unicas)-1)
   else:
      print(0)