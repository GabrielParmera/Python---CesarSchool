import os
os.system("cls")

banho = 0
tosa = 0
banho_e_tosa = 0
outros = 0

for servico in range (0,5):
    print("1 - banho, 2 - tosa, 3 - banho e tosa, 4 - outros")
    servico = int(input("Digite o código do serviço efetuado: "))
    if (servico == 1):
        banho+=1
    elif (servico == 2):
        tosa+=1
    elif (servico == 3):
        banho_e_tosa+=1
    elif (servico == 4):
        outros+=1
    else:
        print("Inválido")

print(f"\nNo total, foram {banho} banhos")
print(f"\nNo total, foram {tosa} tosa")
print(f"\nNo total foram {banho_e_tosa} serviços combinados")
print(f"\nNo total, foram {outros} outros serviços")
