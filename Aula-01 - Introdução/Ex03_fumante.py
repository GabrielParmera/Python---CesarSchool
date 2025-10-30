import os
os.system("cls")
# ATIVIDADE 3
mediaCigarro = int(input("Digite a média de cigarros fumados por dia: "))
anosFumados = int(input("Digite a qtd de anos fumados: "))

total_cigarros = (anosFumados*365)*mediaCigarro
dias_perdidos = (total_cigarros*10)/1440
# 1440 = Minutos em 1 dia
print(f"Até o presente momento, vossa senhoria perdeu {dias_perdidos:.2f} dias.")
