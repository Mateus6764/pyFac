print(f'Escrever um algoritmo em Python que exiba o público total (inteiro) de um jogo de futebol e forneça a arrecadação (R$: real) do jogo.\n')

try:
    crianca = int(input(f'Quantidade de crianças ( < 10 anos): '))
    jovem = int(input(f'Quantidade de jovens ( 11 a 17 anos): '))
    alimento = int(input(f'Quantidade de pessoas (+18) que doaram alimentos: '))
    adulto = int(input(f'Quantidade de adultos (+18) que não doaram alimentos: '))
    
    ingresso = float(input(f'Digite o valor do ingresso: '))
    
    pessoas = crianca + jovem + alimento + adulto
    total =  0 * (crianca * ingresso)
    total =  jovem * (2 / ingresso) 
    total = alimento * (2 / ingresso)
    total = adulto * ingresso
    
    print(f'Número total de pessoas: {pessoas} .')
    print(f'Arrecadação total: {total:.2f} .')
    
except Exception as ERRO_EXC:
    print(f'Erro de exceção: {ERRO_EXC}.')
    