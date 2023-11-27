from datetime import date

ano= date.today().year
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
    print('Master')