from random import choice
N1 = str(input('primeiro aluno: '))
N2 = str(input('segundo aluno: '))
N3 = str(input('terceiro aluno: '))
N4 = str(input('quarto aluno: '))
lista = [N1, N2, N3, N4]
escolhido = choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))


