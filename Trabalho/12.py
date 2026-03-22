soma = 0
contador = 0

print("Digite as temperaturas do verão (<= 28 encerra):")

temperatura = float(input())

while temperatura > 28:
    soma += temperatura
    contador += 1
    temperatura = float(input())

if contador > 0:
    media = soma / contador
    print(f"Temperatura média do verão: {media:.2f}°C")
else:
    print("Nenhuma temperatura válida foi informada.")