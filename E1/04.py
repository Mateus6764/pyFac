print(f'Tendo como dado de entrada a altura (h) e o sexo de uma pessoa, construa um algoritmo que calcule seu peso (Massa: Quilogramas) ideal.\n')

try:
    sexo = input(f'Digite seu sexo (h = homem, m = mulher):')
    
    if sexo == "h":
        print('Homem:')
        altura = float(input(f'Digite sua altura em M: '))
        
        pid = (72.7 * altura) - 58
        print(f'Seu peso ideal é: {pid:.1f}')
        
    elif sexo == "m":
        print('Mulher:')
        altura = float(input(f'Digite sua altura em M: '))
        
        pid = (62.1 * altura) - 44.7
        print(f'Seu peso ideal é: {pid:.1f}')
        
    else:
        print(f'Erro de Entrada.')
        
        
except Exception as ERRO_EXC:
    print(f'Erro de exceção: {ERRO_EXC}.')
    