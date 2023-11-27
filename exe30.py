r1 = float(input('primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos acima podem formar um triângulo')
    if r1==r2 and r2==r3:
        print('Triângulo Equilátero')
    if r1 != r2 != r3 !=r1:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
else:
    print('Os segmentos acima não podem formar um triângulo')