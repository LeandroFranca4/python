km=float(input('quantos kms vc percorreu?:'))
dia=int(input('quantosdias vc alugou o carro?'))
d= 60*dia
k=0.15*km
valor= d+k
print('Km percorrido: {} total a pagar:{}, dias alugado: {}total a pagar{}, valor final {}'.format(km,k,dia,d,valor))
