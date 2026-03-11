print(f'2) Escrever um algoritmo em Python que leia a Base (B > 0) e a Altura (H > 0) de um retângulo em centímetros e calcule e exiba na tela seu Perímetro.\n')

try:
    h = float(input(f'Digite a altura H em cm: '))
    b = float(input(f'Digite a basa B em cm: '))
    
    if h > 0 and b > 0:
        pcm = (h*2) + (b*2)
        pin = pcm / 2.54
        pja = pcm * 0.03
        
        print(f'Perimetro em cm: {pcm:.2f}\n')
        print(f'Perimetro em in: {pin:.2f}\n')
        print(f'Perimetro em jardas: {pja:.2f}\n')
        
    else:
        print(f'Erro de entrada.')
        
except Exception as ERRO_EXC:
    print(f'Erro de exceção: {ERRO_EXC}.')