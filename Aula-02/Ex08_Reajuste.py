import os
os.system("cls")

admissao = int(input("Digite o ano de admissão: "))
AnoAtual = int(input("Digite o ano atual: "))
TempoDeCasa = AnoAtual - admissao
salario = float(input("Digite o salário atual: "))
condicao = float(input("Digite o tempo em anos desde o último aumento: "))

if (condicao < 2):
    print("Não está apto para aumento")
elif (condicao >= 2):
    if(TempoDeCasa < 5):
        novo_salario = (salario * 1.10)
        print(f"Seu novo salário será {novo_salario} reais.")
    elif(TempoDeCasa >=5 and TempoDeCasa <=10):
        novo_salario = (salario * 1.20)
        print(f"Seu novo salário será {novo_salario} reais.")
    else:
        novo_salario = (salario * 1.30)
        print(f"Seu novo salário será {novo_salario} reais.")