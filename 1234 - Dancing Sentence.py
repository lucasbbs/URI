while True:
  try:
    row = input()
  except EOFError:
    break
  if row == "":
    break
  str = ""
  i = 0
  for n in row:
    if n == " ":
      str += ' '
    else:
      if i%2 == 0: str += n.upper()
      else: str += n.lower()
      i += 1
  print(str)

  # while True:
  #   try:
  #       s = list(input())
  #   except EOFError:
  #       break
  #   upper = True
  #   for i, caractere in enumerate(s):
  #       if caractere == ' ':
  #           continue
  #       if caractere.isupper() != upper:
  #           if upper:
  #               s[i] = s[i].upper()
  #           else:
  #               s[i] = s[i].lower()
  #       upper = not upper
  #   print("".join(s))