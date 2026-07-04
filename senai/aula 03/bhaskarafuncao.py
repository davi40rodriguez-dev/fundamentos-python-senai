def raizes(delta1, a1, b1):
    raiz1 = (-b1 + (delta)**0.5 / (2*a1))
    return raiz1

#Entrada de dados
a = float(input("Digite o valor de a: "))
b = float(input ("Digite o valor de b: "))
c = float(input("Digite o valor de c:"))

#Saída de dados 1

print(f"A equação de segundo grau é:\n\t{a}x² + {b}x + c = 0")

#Processamento de dados

delta = (b**2) - (4 * a * c)

#Estrutura de controle de decisão (if)-Verificar se o delta>0


if delta == 0:
    raiz = (-b + (delta)**0.5) / (2 * a)
    print("Raizes iguais, portanto x = ", raiz)

elif delta > 0:
    raiz1 = raizes(delta, a, b)
    raiz2 = (-b - (delta)**0.5) / (2* a)
    print("Raiz 1 = ", raiz1)
    print("Raiz 2 = ", raiz2)
else:
    print("O valor delta é menor que zero, raizes impossiveis!")