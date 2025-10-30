frase = str(input("Digite a frase de referência: "))
palavra = str(input("Escolha uma palavra: "))
novap = str(input("Escolha uma nova palavra: "))

if palavra in frase:
   frase_modificada = frase.replace(palavra, novap).upper()
   print(frase_modificada)
else:
  print("A palavra não está na frase!")