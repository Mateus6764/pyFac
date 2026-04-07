import math

for i in range(1, 501):
    print(f"\nPaciente {i}")

    idade = int(input("Idade: "))
    massa = float(input("Massa: "))
    diabete = input("É diabético? (s/n): ").lower()

    if diabete == 'n':
        taxa = math.sqrt(0.98 * (massa ** 2)) / (1.08 * idade)
    else:
        taxa = math.sqrt(massa ** 2) / (0.93 * idade)

    print(f"Taxa de glicose: {taxa:.2f}")