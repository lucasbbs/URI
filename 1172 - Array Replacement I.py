elements = []
for i in range(10): elements.append(int(input()))
new_list = [1 if int(el)<=0 else el for el in elements]
for n in range(len(new_list)):
  print(f'X[{n}] = {new_list[n]}')