l = float(input('qual a largura da parede: '))
alt = float(input('altura da parede: '))
area = l * alt
print('-' * 12)
print('sua parede tem a dimensao de {}x{} e sua area é de {}'.format(l, alt, area))
tinta = area / 2
print('para pintar essa parede você precisara de {}l de tinta'.format(tinta))
