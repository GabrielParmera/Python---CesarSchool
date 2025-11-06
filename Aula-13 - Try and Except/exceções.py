numeros = []

for i in range(10):
    while True:
        try:
            valor = int(input(f"Digite o {i+1}º número: "))
            numeros.append(valor)
            break  
        except ValueError:
            print("Por favor, digite um número inteiro.")
        except IndexError:
            print("Seu index não existe")

primeiro = numeros[0]
maiores = menores = iguais = 0

for n in numeros:
    if n > primeiro:
        maiores += 1
    elif n < primeiro:
        menores += 1
    else:
        iguais += 1

print(f"Primeiro elemento: {primeiro}")
print(f"Números maiores que o primeiro: {maiores}")
print(f"Números menores que o primeiro: {menores}")
print(f"Números iguais ao primeiro: {iguais}")