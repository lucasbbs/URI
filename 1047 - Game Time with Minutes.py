hour1, min1, hour2, min2 = map(int, input().split())
def calculateDurationGame(hour1, min1, hour2, min2 ):
  if hour2 == hour1 and min2 == min1:
    return('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
  if hour2 == hour1 and min2 < min1:
    return(f'O JOGO DUROU {24 - (hour1-hour2)-1} HORA(S) E {60-(min1 - min2)} MINUTO(S)')
  if hour2 < hour1 and min2 > min1:
    return(f'O JOGO DUROU {24 - (hour1-hour2)} HORA(S) E {min2 - min1} MINUTO(S)')
  if hour2 > hour1 and min2 < min1:
    return(f'O JOGO DUROU {(hour2-hour1)-1} HORA(S) E {60-(min1 - min2)} MINUTO(S)')
  if hour2 < hour1 and min2 < min1:
    return(f'O JOGO DUROU {24 - (hour1-hour2)-1} HORA(S) E {60-(min1 - min2)} MINUTO(S)')
  return(f'O JOGO DUROU {hour2-hour1} HORA(S) E {min2 - min1} MINUTO(S)')
print(calculateDurationGame(hour1, min1, hour2, min2))