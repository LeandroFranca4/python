n=  (int(input('Digite um número:')),
    int(input('Digite um número:')),
    int(input('Digite um número:')),
    int(input('Digite um número:')))
print(f'Você digitou {n}')
print(f'O 9 apareceu {n.count(9)}')
if 3 in n:
    print(f'O número 3 apareceu na {n.index(3)+1} posição')
print('Os valores pares digitados foram:', end='')
for num in n:
    if num % 2 == 0:
        print (num, end='') 