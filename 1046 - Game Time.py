hour1, hour2 = map(int, input().split())
def calculateDurationGame(hour1, hour2 ):
  if hour2 == hour1:
    return('O JOGO DUROU 24 HORA(S)')
  if hour2 < hour1:
    return(f'O JOGO DUROU {24 - (hour1-hour2)} HORA(S)')
  if hour2 > hour1:
    return(f'O JOGO DUROU {(hour2-hour1)} HORA(S)')
print(calculateDurationGame(hour1, hour2))