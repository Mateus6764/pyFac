x = int(input(f'Digite um valor inteir positivo (x >= 1): '))

if x < 1:
    print(f'Valor inválido!')

else:
    cont = 0
    soma = 0
    
    for i in range(6, x * 6 + 1, 6):
        soma += i
        cont += 1
        
    media = soma / cont
    print(f'Média de múltiplos de 6: {media:.2f}')