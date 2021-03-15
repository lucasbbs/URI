N1, N2, N3, N4 = map(float, input().split())
media = (N1*2+ N2*3 + N3*4 +N4*1)/10
print(f'Media: {media:.1f}')
if media >= 7:
  print('Aluno aprovado.')
elif media >= 5  and media < 7:
  print('Aluno em exame.')
  newExam = float(input())
  print(f'Nota do exame: {newExam:.1f}')
  if (media+newExam)/2 >= 5:
    print('Aluno aprovado.')
  else:
    print('Aluno reprovado.')
  print(f'Media final: {(media+newExam)/2:.1f}')
else:
  print('Aluno reprovado.')