a = int(input("Digite o 1º termo: "))
b = int(input("Digite o 2º termo: "))
c = int(input("Digite o 3º termo: "))

print(a, b, c, end=" ")

for i in range(20):
    d = a + b + c
    print(d, end=" ")
    
    a = b
    b = c
    c = d