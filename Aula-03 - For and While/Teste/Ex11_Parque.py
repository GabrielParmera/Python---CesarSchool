import os
os.system("cls")

visitantes = int(input("Digite a qtd de visitante: "))
altMax = float(input("Digite a altura máxima: "))
altMin = float(input("Digite a altura Mínima: "))

pode=0
Npode=0

for i in range(0, visitantes):
    altura = float(input("Digite a altura do visitante: "))
    if (altura < altMin and altura > altMax):
        print("Ele(a) não é capaz de ir na Montanha-Russa")
        Npode+=1
    else:
        print("Ele(a) pode ir na Montanha-Russa")
        pode+=1

print(f"A qtd de visitante que podem ir na atração é de {pode}, enquanto a qtd de visitantes que não podem é {Npode}.")