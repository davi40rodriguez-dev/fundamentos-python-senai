RESP1 = "Quantos casos você vai digitar? " #Variavel constante


try:
 #Entrada de dados
    n = int(input(RESP1))
    for i in range (n):
        x = float(input("Digite o numerador?"))
        y = float(input("Digite o denominador?"))
        if (y == 0):
            print("Divisão impossivel")
    else:
    #Processamento de Dados
        resultado = x / y
    #Saída de dados
    print(f"Divisão = {resultado:.2f}")
except:
    print("Digite valores validos! :")