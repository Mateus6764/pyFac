def ler_num():
    while True:
        n = int(input('Digite um número entre 2 e 1000: '))
        if 2 <= n <= 1000:
            return n
        else:
            print('Valor fora do intervalo')


def primo(n):
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

def resultado(n):
    if primo(n):
        print(f'{n} é um número primo.')
        
    else:
        print(f'{n} não é um número primo.')
        

numero = ler_num()
resultado(numero)