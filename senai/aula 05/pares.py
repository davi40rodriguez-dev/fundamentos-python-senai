def clodoaldo(X):
    resultado = x + (x+2) + (x+4) + (x+6) + (x+8)
    print(f"Soma = {resultado}")
x:int

while (x!=0):
    x = int(input("Digite um numero inteiro: "))
    if x == 0:
        break

    if (x%2) == 0:
        print("Numero PAR")
        clodoaldo(x)
else:
    print("Número IMPAR")
    resultado = (x+1) + (x+2) + (x+4) + (x+6) + (x+8)
    print(f"soma = {resultado}")
