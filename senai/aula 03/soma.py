try:
    #entrada de dados
    x = int(input("Digiteno valor de x:"))
    y = int(input("Digite o valor de y:"))
    
    #Processamento de dados

    soma = x % y

    #Saída de dados
    print(f"A soma é de {soma}")
except:
  print("Erro: Digite um valor válido")

