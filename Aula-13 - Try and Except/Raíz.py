import math

while True:
   try:
        numero = int(input("Digite um número para obter a raíz: "))
        raiz = math.sqrt(numero)
        print(f"Raíz do número {numero} é {raiz:.2f}")
        break
   except ValueError:
        print("Um número inteiro, por favor")
        continue
    