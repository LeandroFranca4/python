

mhomem=0
nvelho=''

for p in range (1,3):
    print('-----{} pessoa-----'.format(p))
    nome=str(input('Nome:')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]:')).strip()
   
    if p==1 and sexo in 'Mm':
        mhomem=idade  
        nvelho=nome 
    if sexo in 'Mm' and idade>mhomem:
        mhomem= idade
        nvelho= nome
    

print('Homem mais velho {} e nome {}'.format(mhomem,nvelho))


