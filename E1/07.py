import math

try:
    a = float(input(f'Digite o Lado: '))
    area = a ** 2
    
    print(f'A area é: {area:.2f}')

except Exception as ERRO_EXC:
    print(f'Erro de exceção: {ERRO_EXC}.')
    