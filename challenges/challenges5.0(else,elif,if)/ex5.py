not1 = float(input('primeira nota: '))
not2 = float(input('segunda nota: '))
media = (not1 + not2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(not1, not2, media))
if 7 > media >=5:
    print('O aluno está em RECUPERAÇAO.')
elif media < 5:
    print('O aluno foi REPROVADO')
elif media >=7:
    print('o aluno esta APROVADO')

















