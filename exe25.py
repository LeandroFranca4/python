

'''ano= 2023
idade = int(input('Digite o ano que você nasceu:'))
n1= ano-idade
if n1 <= 9:
    print('Mirim')
elif n1<=14:
    print ('infantil')
elif n1<=19:
    print('Junior')
elif n1 <=20:
    print('Sênior')
else:
    print('Master')'''


from datetime import date
atual=date.today().year

print('[1] para masculino [2] para feminino ')
sexo=int(input('escolha uma das opções acima:'))
nasc= int(input('Ano de nascimento:'))
idade= atual-nasc
print('Quem nasceu em {}, tem {} anos em {}'.format(nasc, idade, atual))

if sexo == 2:
    print('Você não precisa se alistar')
else:
    print('continue')
if idade == 18 and sexo==1:
    print('Você precisa se alistar')
elif idade < 18:
    saldo= 18-idade
    print('ainda faltam {} anos para se alistar'.format(saldo))
elif idade > 18:
    saldo= idade-18
    print('já passou {} ano, você precisa se alistar'.format(saldo))
    data=atual-saldo
    print('Seu alistamento foi em {}'.format(data))
 

