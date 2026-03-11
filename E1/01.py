import math

print(f'1) Escrever um algoritmo em Python que determine o volume e a área de uma esfera de raio r:\n')

try:
    pi = math.pi
    r = float(input('Digite o ráio da esfera metros: '))
    area = 4 * pi * r ** 2
    volume = 4/3 * pi * r ** 3 
    print(f'A área da esfera em metros quadrados é: {area:.2f}\n ')
    print(f'O volume da esfera em metros cúbicos é: {volume:.2f}\n ')
    
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
    