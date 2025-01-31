nome = str(input('Qual é seu nome? '))
if nome == 'pedro':
    print('Que nome bonito! ')
elif nome == 'Joao' or nome == 'Maria' or nome == 'Gustavo':
    print('seu nome e bem popular no brasil! ')
else:
    print('seu nome é bem normal')
print('prazer em te conhecer {}!'.format(nome))