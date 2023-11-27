'''ano=2023
for s in range(1,8):
    idade=int(input('Digite o ano a {} pessoa nasceu'.format(s)))
    n=ano-idade
    if idade >= 18:
        print('Você é menor')
    else:
        print('Você é maior')'''

from datetime import date
data=date.today().year
totmaior=0
totmenor=0
for pes in range(1,8):
    nasc=int(input('Em que ano você nasceu:'))
    idade=data-nasc
    if idade>= 18:
        totmaior = totmaior+1
    else:
        totmenor += 1

print('TEm {} pessoas maior e {} menor'.format(totmaior, totmenor))


  
