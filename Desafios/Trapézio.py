n = int(input("Número de trapézios: "))
intervalo = []

intervalo.append(int(input()))
a = intervalo[0]
intervalo.append(int(input()))
b = intervalo[1]

h = (b - a)/n

def f(x):
    imagem = 2.71**x**2
    return imagem

soma = 0
for x in range(n):
    base = h * x
    if x != 0 and x!= n:
        soma = soma + f(base)  

area = (h/2) * ((f(a) + f(b)) + (2*soma))
print(f"{area:.3f}")  