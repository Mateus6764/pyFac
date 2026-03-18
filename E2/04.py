soma = 0
quant = 0
maior = 0
menor = 0
media = 0
while True:
    peso = float(input('Digite o peso do boi (0 encerra): '))
    
    if peso == 0:
        break
    
    soma += peso
    quant += 1
    
    if quant == 1:
        maior = peso
        menor = peso
        
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
            
if quant > 0:
    media = soma / quant

    print(f'Peso médio do rebanho {media:.2f}')
    print(f'Maior peso {maior}kg')
    print(f'Menor peso {menor}kg')
    
else:
    print(f'Nenhum peso foi inserido.')