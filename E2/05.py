for i in range(51):
    stop = input('Encerra: <stp> Prosegue:<Enter> (no fim de cada ciclo):')
    
    if stop == 'stp':
        break
    else:
        a = float(input(f'Digite a altura do {i+1}° retângulo: '))
        b = float(input(f'Digite a base do {i+1}° retângulo: '))
        
        area = a * b
        per = 2*(a + b)
            
        print(f'Área do retângulo: {area:.2f}')
        print(f'Perímetro do retângulo: {per:.2f}\n')