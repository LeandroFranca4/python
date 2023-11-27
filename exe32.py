import math

preço=float(input('Qual valor do produto?:'))
print('''Escolha uma das formas de pagamento 
      [1] à vista
      [2] à vista no cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')
opção = int(input('Qual é a forma de pagamento?'))
if opção == 1:
    total= preço - (preço * 10 / 100)
elif opção == 2:
    total= preço - (preço * 5/100)
elif opção ==3:
    total=preço
    parcela = total / 2
    print(' Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total= preço +(preço * 20/100)
    totparc=int(input('quantas parcelas:'))
    parcela=total/totparc
    print('Sua compra será parcelada em {} vezez e o valor ficará {}'.format(totparc, parcela))
print(' O valor da sua compra foi de {:.2f}, com desconto fica {:.2f}'.format(preço, total))