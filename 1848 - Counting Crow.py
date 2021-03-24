for i in range(3):
  result = 0
  while True:
    str = input()
    if str == "caw caw":
      break
    else:
      str = str.replace("-", "0")
      str = str.replace("*", "1")
      str = "0b"+str
      result += int(str,2)
  print(result)