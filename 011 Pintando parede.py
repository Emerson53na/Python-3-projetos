b = float(input('Àrea da parede: '))
h = float(input('Altura da parede: '))
a = b * h
print('A área da parede é de {}m².\nPara pintar a parede, você precisará de \033[32m{}l\033[m de tinta.'.format(a,(a/2)))
