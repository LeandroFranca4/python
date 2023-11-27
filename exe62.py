n=[]
pa=[]
im=[]
while True:
    n.append(int(input('Digite um número:')))
    resp=str(input('Deseja continuar?[S/N]:'))
    if resp in 'Nn':
        break
for i, v in enumerate(n):
    if v % 2 == 0:
        pa.append(v)
    else:
        im.append(v)
print(f'lista {n}')
print(f'pares {pa}')
print(f'impares {im}')
