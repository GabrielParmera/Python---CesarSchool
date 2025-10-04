import os
os.system("cls")

vasc = int(input("A planta possui vascularização? (1 - Sim/ 0 - Não): "))
sementes = int(input("A planta possui sementes? (1 - Sim/ 0 - Não): "))
flor = int(input("A planta possui flores? (1 - Sim/ 0 - Não): "))

if (vasc == 0 and sementes == 0 and flor == 0):
    print("A planta é uma briófita.")
elif (vasc == 1 and sementes == 0 and flor == 0):
    print("A planta é uma pteridófita.")
elif (vasc == 1 and sementes == 1 and flor == 0):
    print("A planta é uma gimnosperma.")
elif (vasc == 1 and sementes == 1 and flor == 1):
    print("A planta é uma angiosperma.")
else:
    print("Não se classifica nesses tipos.")