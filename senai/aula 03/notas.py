#Entrada de dados
nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota:"))

#Processamento de dados
soma = nota1 + nota2

#Saída de dados
print("Nota final: ", soma)

#Estrutura de controle de decisão if (se)
if soma < 60:
    print("Reprovado")
    print("Boa Sorte!")
if soma > 60:
    print("Aprovado")
    print("MUITO BEM!")