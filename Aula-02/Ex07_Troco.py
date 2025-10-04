import os
os.system("cls")

valor = float(input("Digite o valor total da compra: R$ "))
pagamento = float(input("Digite o valor pago pelo cliente: R$ "))

troco = pagamento - valor

if troco < 0:
    falta = valor - pagamento
    print(f"Valor insuficiente. Faltam R$ {falta:.2f} para completar a compra.")
elif troco == 0:
    print("Pagamento exato. Não há troco a devolver.")
else:
    print(f"O troco será: R$ {troco:.2f}")
