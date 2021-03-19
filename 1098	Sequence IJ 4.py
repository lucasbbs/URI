for i in range(0, 11):
  for j in range(1,4):
    print(f'I={.2*i:.1f} J={i*.2 + j:.1f}') if i*.2%1 != 0 and j*.2%1 != 0 else print(f'I={.2*i:.0f} J={i*.2 + j:.0f}') 