peso=float(input('Qual é o seu peso?:'))
altura=float(input('Qual é sua altura?:'))
imc= peso / (altura**2)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc< 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Você está com sobrepeso')
elif 30 <= imc < 40:
    print('seu apelido é gordão')
else:
    print ('BALEIAAAAAAAAAAAAAAAAAAAAAA')

