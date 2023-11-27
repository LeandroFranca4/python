n=int(input('Digite um número:'))
u= n // 1 % 10
d= n // 10 % 10
c= n // 100 % 10
m= n // 1000 % 10
print('analisando número:{}'.format (n))
print('unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))