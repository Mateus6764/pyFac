print(f'3) Faça um algoritmo em Python que leia o tempo (segundos) de permanência de um aluno no Laboratório de Programação: UVV e exiba na tela seu tempo de permanência: Horas + Minutos + Segundos.\n')

try:
    tempo = int(input(f'Digite o tempo de permanência do aluno em segundos: '))
    
    horas = tempo // 3600
    resto = tempo % 3600
    minutos = resto // 60
    segundos = resto % 60
    
    print(f"Tempo: {tempo} Segundos = {horas} Hora(s) + {minutos} Minuto(s) + {segundos} Segundo(s)")
    
except Exception as ERRO_EXC:
    print(f'Erro de exceção: {ERRO_EXC}.')
    
    