nome=str(input ('Digite seu nome:')).strip() #strip anula os espaços laterais 
print ('Seu nome é:{}'.format(nome))
print('Seu nome em letras maiúsculas:', nome.upper()) 
print ('Seu nome em letras minúsculas:', nome.lower())
print('Seu nome tem ao todo {} letras'.format (len(nome)-nome.count(' ')))
#print ('Seu primeiro nome tem {} letras'.format(nome.find(' '))) // primeira forma de mostrar quantas letras tem somente o primeiro nome
separa= nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


