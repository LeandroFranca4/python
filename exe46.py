from time import sleep
n1=int(input('Digite um número:'))
n2=int(input('Digite outro número:'))
opção = 0
while opção != 5:
    print('''[1] Somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa''')
    opção=int(input('Qual é a opção?'))
    if opção==1:
        r=n1+n2
        print('Resultado {}'.format(r))
    elif opção==2:
        r=n1*n2
        print('Resultado {}'.format(r))
    elif opção ==3:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opção==4:
        print('informe os números novamente')
        n1=int(input('Digite um número:'))
        n2=int(input('Digite um número:'))
    elif opção==5:  

        print('fim do programa')

