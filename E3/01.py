def menu():
    print(f'\n--- Calculadora ---')
    print('1 - Entrada de dados')
    print('2 - Adição')
    print('3 - Subtração')
    print('4 - Multiplicação')
    print('5 - Divisão')
    print('6 - Encerra')
    
def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return  a * b

def verif_div_zero(b):
    return b==0

def dividir(a, b):
    if verif_div_zero(b):
        return "Erro: Divisão por Zero!"
    return a / b

num1 = None
num2 = None

while True:
    menu()
    opcao = input('Escolha uma das opções: ')
    
    if opcao == '1':
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segndo número: '))
        
    elif opcao == '2':
        if num1 == None or num2 == None:
            print('Primeiro insira os dados!')
            
        else:
            print(f'Resultado: {adicionar(num1, num2)}')
            
    elif opcao == '3':
        if num1 == None or num2 == None:
            print('Primeiro insira os dados!')
            
        else:
            print(f'Resultado: {subtrair(num1, num2)}')
            
    elif opcao == '4':
        if num1 == None or num2 == None:
            print('Primeiro insira os dados!')
            
        else:
            print(f'Resultado: {multiplicar(num1, num2)}')
            
    elif opcao == '5':
        if num1 == None or num2 == None:
            print('Primeiro insira os dados!')
            
        else:
            print(f'Resultado: {dividir(num1, num2)}')
            
    elif opcao == '6':
        print('Encerrando...')
        break
    
    else:
        print('Opção inválida!')