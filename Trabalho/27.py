soma_pos = 0
qtd_pos = 0

soma_neg = 0
qtd_neg = 0

print("Digite números reais (0 encerra):")

numero = float(input())

while numero != 0:
    if numero > 0:
        soma_pos += numero
        qtd_pos += 1
    else:
        soma_neg += numero
        qtd_neg += 1

    numero = float(input())

# Cálculo das médias
if qtd_pos > 0:
    media_pos = soma_pos / qtd_pos
    print(f"Média dos positivos: {media_pos:.2f}")
else:
    print("Nenhum número positivo foi informado.")

if qtd_neg > 0:
    media_neg = soma_neg / qtd_neg
    print(f"Média dos negativos: {media_neg:.2f}")
else:
    print("Nenhum número negativo foi informado.")