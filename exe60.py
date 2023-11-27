número= []
while True:
    n=(int(input('Digite um número:')))
    if n not in número:
        número.append(n)
        print('número adicionado:')
    else:
        print('Número repetido...')

    o=str(input('Deseja continuar[S/N]:'))
    if o in 'Nn':
        break
    
número.sort()
print(f'Você digitou {número}')