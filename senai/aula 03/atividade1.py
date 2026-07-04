try:
    #entrada de dados
    dias = int(input("digite quantos dias você viveu: "))

    #processamento de dados
    ano = dias // 365
    mes = (dias % 365) // 30
    dia = (dias % 365) % 30 

    #Saída de dados
    print(f"ano(s) é igual a:{ano}")
    print(f"mes(es) é igual a:{mes}")
    print(f"dia(s) é igual a:{dia}")
except:
    print("digite algo valido")