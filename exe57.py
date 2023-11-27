palavras=('aprender','programador','pinto','python','curso')

for p in palavras:
    print(f'\n na palavra {p} temos ' , end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l , end=' ')

