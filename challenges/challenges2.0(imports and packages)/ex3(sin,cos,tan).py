import math
ang = float(input('digite o angulo que voce deseja: '))
seno = math.sin(math.radians (ang))
print('o angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
cos = math.cos(math.radians(ang))
print('o angulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
tan = math.tan(math.radians(ang))
print('o angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))
