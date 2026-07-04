#Entrada de dados
glicose = float(input("Digite a sua glicose: "))

#Processamento de dados
#Estrutura de controle de decisão - IF ELIF ELSE
if glicose <= 100:
    saida = "Normal"
elif(glicose > 100) or (glicose <= 140):
    saida = "elevado"
else:
    saida = "DIabetes"

#Saída de dados
print(f"Classificação: {saida}")