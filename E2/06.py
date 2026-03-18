maior = 0
segundo_maior = 0

while True:
    num = int(input("Digite um número positivo (0 para encerrar): "))

    if num == 0:
        break

    if num > maior:
        segundo_maior = maior
        maior = num
    elif num > segundo_maior:
        segundo_maior = num

print("Maior número:", maior)
print("Segundo maior número:", segundo_maior)