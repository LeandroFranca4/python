'''valores=[]
for cont in range (0,5):
    valores.append(int(input('Digite um valor:')))  #EU QUE FIZ
print(valores)
print(f'O maior valor foi {max(valores)}')
print(f'O menor foi {min(valores)}')
'''

valores = []
mai = 0
men = 0
for c in range (0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}:')))
    if c == 0:
        mai = men = valores [c]
    else:
        if valores [c] > mai:
            mai = valores [c]
        if valores [c] < men:
            men = valores[c]
print(f'Os números digitados foram {valores}')
print(f'O maior foi {mai} na posição ')
for i, v in enumerate (valores):
    if v == mai:
        print(f'{i}')
print(f'O menor foi {men} na posição ')
for i, v in enumerate (valores):
    if v == men:
        print(f'{i}')
            




