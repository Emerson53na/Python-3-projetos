a = int(input(' A = '))
b = int(input(' B = '))
c = int(input(' C = '))

d1 = b**2
d2 = (-4)*a*c
d = d1+d2
delta = d
print('\033[33m ∆\033[m = {:.2f}'.format(delta))

if delta >= 0:
    xi = -(b)+(delta**(1/2))
    x1 = xi/(a*2)
    print('\033[32m X1\033[m = {:.2f}'.format(x1))
    xii = -(b)-(delta**(1/2))
    x2  = xii/(a*2)
    print('\033[32m X2\033[m = {:.2f}'.format(x2))
