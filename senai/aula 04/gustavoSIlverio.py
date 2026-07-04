#Entrada de dados
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))
#Processamento de dados
soma = a + b
perimetro = (a + b + c)
area = ((a + b) * c) / 2
if soma < c:
    saida = perimetro
elif soma < c:
    saida = area
#Saída de dados
if soma > c:
    print(f"Perímetro = {saida}")
elif some < c:
    print(f"Área = {saida}")