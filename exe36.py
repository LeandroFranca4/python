soma=0
for x in range(1,501,2):
    if x % 3==0:
        soma=soma+x
print('A soma dos números {}'.format(soma))