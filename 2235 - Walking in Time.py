a, b, c = map(int, input().split())

if a == b or a == c or b==c or abs((a-b)) == c \
or abs((c-a)) == b or abs((c-b)) == a  or (a+b) == c\
or a+c ==b or b+c ==a:
  print('S')
else:
  print('N')