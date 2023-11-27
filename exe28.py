from random import randint

it=('pedra','papel','tesoura')
comp=randint(0,2)
print('''
[0] pedra
[1] papel
[2] tesoura'''
      )
jog=int(input('escolha:'))
print('computador jogou:{}' .format(it[comp]))
print('jogador: {}'.format(it[jog]))

if jog==comp:
    print('empate')
elif jog==0 and comp==1:
    print('O computador venceu')
elif jog==0 and comp==2:
    print('Você venceu')

elif jog==1 and comp==0:
    print('Você ganhou')
elif jog==1 and comp==2:
    print('Você perdeu')
    
elif jog==2 and comp==1:
    print('Você ganhou')
elif jog==2 and comp==0:
    print('Você perdeu')


