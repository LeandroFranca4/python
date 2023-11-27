soma=0
cont=0

n1=int(input('Digite um número:'))
n2=str(input('Quer continuar?[S/N]')).upper()
while n2=='S':
    n1=int(input('Digite um número:'))
    soma=soma+n1
    n2=str(input('Quer continuar?[S/N]')).upper()
   
    
if n2=='N':
        print('Fim {}'.format(soma))
    