n = int(input("Digite um valor para n (>=5): "))

while n < 5:
    n = int(input("Valor inválido. Digite n >= 5: "))

soma = 0

for k in range(1, n + 1):
    soma += 6 / (k ** 2)

print("Valor de S =", soma)