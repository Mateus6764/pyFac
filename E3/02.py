import math

def area(r):
    return math.pi * (r**2)

r = float(input('Digite o Raio do círculo: '))
print(f'Resultado: {area(r):.2f}')