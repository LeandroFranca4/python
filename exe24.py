n1=float(input('Nota do aluno atividade 1:'))
n2=float(input('Nota do aluno na prova:'))

r= (n1+n2)/2
if r< 5.0:
    print('A média do aluno foi {}.Reprovado'.format(r))
elif r<= 6.9:
    print('A média do aluno foi {}.Recuperação'.format(r))
else:
    print('A média do aluno foi {}.aprovado'.format(r))
