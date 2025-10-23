vogais = []

frase = str(input("Digite uma frase: "))
for letra in frase:
    if letra.lower() in 'aeiou':
        vogais.append(letra.lower())
print("As vogais encontradas foram:", vogais)
print("Total de vogais encontradas:", len(vogais))
print("A letra 'a' apareceu", vogais.count('a'), "vezes.")
print("A letra 'e' apareceu", vogais.count('e'), "vezes.")
print("A letra 'i' apareceu", vogais.count('i'), "vezes.")
print("A letra 'o' apareceu", vogais.count('o'), "vezes.")
print("A letra 'u' apareceu", vogais.count('u'), "vezes.")