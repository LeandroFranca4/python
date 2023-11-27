from random import randint
comp=randint(1,11)
acertou=False
palpite=0
while not acertou:
    jog=int(input('Digite um número de 1 a 10:'))
    palpite=palpite+1
    if jog==comp:
        acertou=True
    else:
        if jog>comp:
            print('menooor')
        else:
            print('maiooor')
print('acertou')
print('{}'.format(palpite))