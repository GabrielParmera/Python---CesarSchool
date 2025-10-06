num = []
par = []
impar = []

for i in range(10):
    nm = int(input("Digite um número (0 para parar): "))
    num.append(nm)

for nm in num:
    if nm % 2 == 0:
        par.append(nm)
    else:
        impar.append(nm)

print(f"Números: {num}")
print(f"Números pares: {par}")
print(f"Números ímpares: {impar}")