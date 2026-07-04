import time
from colorama import Fore, Style, init

# Inicia o colorama
init(autoreset=True)

print(Fore.YELLOW + "Aplicativo de controle de fluxo carros")
print(Fore.GREEN + "Parque Nacional os Lençóis Maranhenses\n")

total_turistas = 0

print(Fore.CYAN + "Bem-vindo ao aplicativo de controle de fluxo de carros!")

while True:
    fluxo = input(
        Fore.WHITE +
        "\nDigite o fluxo de carro (entrada/saida)\n"
        "ou sair para encerrar a aplicação: "
    ).lower()

    if fluxo == "sair":
        print(Fore.YELLOW + "\nSaindo do aplicativo...")
        print(Fore.GREEN + "Aplicativo encerrado.")
        break

    elif fluxo == "entrada":
        try:
            numero = int(input("Digite o número de turistas: "))
            total_turistas += numero

            print(Fore.BLUE + f"\nEntrada registrada em: {time.ctime()}")
            print(Fore.GREEN + f"Entrada de {numero} turistas registrada.")
            print(Fore.GREEN + f"Total de turistas no parque: {total_turistas}")

        except ValueError:
            print(Fore.RED + "Erro: Digite um número válido.")

    elif fluxo == "saida":
        try:
            numero = int(input("Digite o número de turistas: "))

            if numero > total_turistas:
                print(Fore.RED + "Erro: Não há turistas suficientes no parque.")
            else:
                total_turistas -= numero
                print(Fore.BLUE + f"\nSaída registrada em: {time.ctime()}")
                print(Fore.GREEN + f"Saída de {numero} turistas registrada.")
                print(Fore.GREEN + f"Total de turistas no parque: {total_turistas}")

        except ValueError:
            print(Fore.RED + "Erro: Digite um número válido.")

    else:
        print(Fore.RED + "Erro: Por favor, digite 'entrada' ou 'saida'.")