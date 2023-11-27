from random import randint
num=(randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram:')
for n in num:
    print(n)
print(f'O maior valor sorteado foi: {max(num)}')
print(f'O maior valor sorteado foi: {min(num)}')
