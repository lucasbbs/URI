import datetime
day1 = input()
time1 = input()
day2 = input()
time2 = input()

h1, m1, s1 = map(int, time1.split(' : '))
h2, m2, s2 = map(int, time2.split(' : '))

numeric_filter = filter(str.isdigit, day1)
day1 = int("".join(numeric_filter))
numeric_filter = filter(str.isdigit, day2)
day2 = int("".join(numeric_filter))

date1 = datetime.datetime(2021, 1, day1,h1, m1, s1 )
date2 = datetime.datetime(2021, 1, day2,h2, m2, s2 )

print(f'{(date2 - date1).days} dia(s)')
print(f'{(date2 - date1).seconds//3600} hora(s)')
print(f'{(date2 - date1).seconds%3600//60} minuto(s)')
print(f'{(date2 - date1).seconds%3600%60} segundo(s)')