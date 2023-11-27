while True:
    n= int(input('Digite um número:'))
    if n < 0:
            break
    for c in range (1,11):
        r=n*c
        print('{} x {}= {}'.format(n, c, r ))
        