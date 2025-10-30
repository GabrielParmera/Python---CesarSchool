import os
os.system("cls")


animais = []
reptil = []
mamifero = []
ave = []
outro = []

for i in range (10):
  animal = input("Digite o animal: ")
  animais.append(animal)
  categoria = int(input("Digite a categoria: "))
  if categoria == "1":
    reptil.append(animal)
  elif categoria == "2":
    mamifero.append(animal)
  elif categoria == "3":
    ave.append(animal)
  elif categoria == "4":
    outro.append(animal)
  else:
    print("Categoria Inválida")

print(f"Número de répteis -> ({len(reptil)}): {reptil}")
print(f"Número de mamíferos -> ({len(mamifero)}): {mamifero}")
print(f"Número de aves -> ({len(ave)}): {ave}")
print(f"Outros -> ({len(outro)}): {outro}")