lista=('Lápis', 1.50,
       'borracha', 2.00,
       'Caderno', 20.00,
       'estojo', 7.50,
       'caneta', 3.00)
print(lista)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print('{}'.format(lista[c]))
    else:
        print('R$ {}'.format(lista[c]))