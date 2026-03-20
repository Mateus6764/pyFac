salario_min = 1518.0
A = 0
B = 0
C = 0

for i in range(1000):
    salario = float(input(f'Digite o salário do cliente {i+1}:'))
    
    if salario >= 15 * salario_min:
        A += 1
        
    elif salario >= 5 * salario_min:
        B += 1
        
    else:
        C += 1
        
print("\n--- RESULTADO ---")
print(f"Tipo A: {(A / 1000) * 100:.2f}%")
print(f"Tipo B: {(B / 1000) * 100:.2f}%")
print(f"Tipo C: {(C / 1000) * 100:.2f}%")