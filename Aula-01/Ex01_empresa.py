nome = input("Digite o nome do cliente: ")
num = int(input("Digite o número do pedido: "))
valor = float(input("Digite o valor da compra: "))
forma = input("O pagamento será parcelado ou à vista? ")

print(f"\nO cliente {nome} realizou um pedido de número {num} no valor de R${valor}, e o seu pagamento será {forma}")