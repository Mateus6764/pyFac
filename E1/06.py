import math

try:
    b = float(input(f'Digite o cateto B: '))
    c = float(input(f'Digite o cateto C: '))
    h = math.sqrt(b**2 + c**2)
    
    print(f'A hipotenusa é: {h:.2f}')

except Exception as ERRO_EXC:
    print(f'Erro de exceção: {ERRO_EXC}.')
    