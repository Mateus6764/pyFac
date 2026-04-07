vip = 0
standard = 0
total = 0

opcao = 1

while opcao != 0:
    print("\n1 - Cadastrar cliente")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        salario = float(input("Digite o salário do cliente: "))

        if salario >= 5000:
            vip += 1
        else:
            standard += 1

        total += 1

    elif opcao != 0:
        print("Opção inválida!")

# Cálculo das porcentagens
if total > 0:
    perc_vip = (vip / total) * 100
    perc_standard = (standard / total) * 100

    print("\n--- Resultado ---")
    print(f"Cartão VIP: {perc_vip:.2f}%")
    print(f"Cartão STANDARD: {perc_standard:.2f}%")
else:
    print("Nenhum cliente foi cadastrado.")