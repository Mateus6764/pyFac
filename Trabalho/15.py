positivos = 0
negativos = 0
total = 0

print("Digite números reais (0 encerra):")

numero = float(input())

while numero != 0:
    if numero > 0:
        positivos += 1
    else:
        negativos += 1

    total += 1
    numero = float(input())

if total > 0:
    perc_positivos = (positivos / total) * 100
    perc_negativos = (negativos / total) * 100

    print(f"Positivos: {perc_positivos:.2f}%")
    print(f"Negativos: {perc_negativos:.2f}%")
else:
    print("Nenhum número válido foi informado.")