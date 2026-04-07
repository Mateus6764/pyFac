soma = 0
contador = 0

print("Digite 100 números que sejam ímpares e múltiplos de 7:")

while contador < 100:
    numero = int(input())

    if numero % 2 != 0 and numero % 7 == 0:
        soma += numero
        contador += 1
    else:
        print("Número inválido! Deve ser ímpar e múltiplo de 7.")

media = soma / 100

print(f"Média dos números: {media:.2f}")