soma=0
cont=0
while True:
    n=int(input('Digite um número(999 para parar):'))
    if n == 999:
        break
    soma=soma+n
    cont+=1
print(f'A soma é {soma} e você digitou {cont}')
    
   
    