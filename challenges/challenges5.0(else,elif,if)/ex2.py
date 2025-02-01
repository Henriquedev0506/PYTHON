n = int(input('digite um numero para converter...'))
print('''escolha uma das bases de conversao: '
      [ 1 ] converter para BINÁRIO
      [ 2 ] converter para OCTAL
      [ 3 ]converter para HEXADECIMAL''')
opcao = int(input('Sua opçao: '))
if opcao == 1:
    print('{} conertido para binario é igual a {}'.format(n,bin(n)[2:]))
elif opcao == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(n, oct(n) [2:]))
elif opcao == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(n, hex(n) [2:]))
else:
    print('Opcao invalida. tente novamente')
