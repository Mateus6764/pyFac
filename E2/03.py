cont = 0
soma = 0
while True:
    num = int(input('Digite um número (digite 0 ou um valor negativo para encerrar):'))
    
    if num <= 0:
        break
    
    else: 
        soma += num
        cont += 1
    
if cont > 1:
    media = soma / cont
    print(f'Média aritmética:', media)

else:
    print(f'O programa não registrou entrada válida')