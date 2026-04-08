
def numPerfeito(valor):
    soma = 0
    for i in range (1, valor // 2 + 1):
        if valor % i == 0:
            soma += i
        
    if soma == valor:
        return True
        
    else:
        return False

for i in range (1,10000):
    if (numPerfeito(i)):
        print(i)