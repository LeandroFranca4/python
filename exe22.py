from random import randint

print('Pense em um número de 0 a 5')
comp = randint (0,5)
jog=int(input('Digite um número de 0 a 5 :'))
if jog==comp:
    print('Parabéns, você é o carro bixo')
else:
    print ('qué, qué, seu número {}, número do computar {}'.format(jog, comp))