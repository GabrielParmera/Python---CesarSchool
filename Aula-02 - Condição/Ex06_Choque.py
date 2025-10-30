import os
os.system("cls")

level = int(input("Digite o nível de Voltorb: "))

if (level < 1 or level > 100):
    print("Inválido")
elif (level >= 1 and level <= 20):
    potencia = (20 + (level * level * level))
    print(f"O choque terá potência de {potencia} W.")
elif (level >= 21 and level <= 40):
    potencia = (8000 + ((level - 10) * (level -10)))
    print(f"O choque terá potência de {potencia} W.")
elif (level >= 41 and level <= 60):
    potencia = (9000 + (5 * level))
    print(f"O choque terá potência de {potencia} W.")
elif (level >= 61 and level <= 80):
    potencia = (9300 + (2 * level))
    print(f"O choque terá potência de {potencia} W.")
elif (level >= 81 and level <= 100):
    potencia = (9500 + level)
    print(f"O choque terá potência de {potencia} W.")