import math

def area(r):
    return math.pi * (r**2)

def volume(r, a):
    return area(r) * a

r = float(input('\n\n\tDigite o valor do raio do cilindro: '))
a = float(input('\n\n\tDigite o valor da altura do cilindro: '))

vol_c = volume(r, a)

print(f'\n\n\tResultado: {vol_c:.2f}')