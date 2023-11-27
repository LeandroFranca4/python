print('===========')
print('JVL viajens')
print('===========')

while True:
    n1=float(input('Digite a distância em km da sua viagem:'))
    if n1<300:
         r=n1*1.10
         print('Sua viagem é de {} Km  e custará R${:.2f}'.format(n1,r))
         s=str(input('Deseja sair?[S/N]:')).upper()
         if s=='S':
              print('Volte sempre')
              break
    elif n1>300:
         r=n1*0.60
         print('Sua viagem é de {} Km  e custará R${:.2f}'.format(n1,r))
         s=str(input('Deseja sair?[S/N]:')).upper()
         if s=='S':
              print('Volte sempre')
              break