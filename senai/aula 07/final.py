 

import random

# Entrada de dados 
print("𝔍𝔬𝔤𝔬 𝔡𝔢 𝔞𝔡𝔦𝔳𝔦𝔫𝔥𝔞𝔯 𝔬 𝔫𝔲́𝔪𝔢𝔯𝔬🫵🏻")
while True:
    numero_secreto = random.randint(1, 10)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Informe um número de 1 a 10: "))

            if palpite < 1 or palpite > 10:
                print("Digite um número válido entre 1 e 10.")
                continue

            tentativas += 1

# Saída de dados 

            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                if tentativas == 1:
                    print("Incrível! Você acertou de primeira!")
                else:
                    print(f"Parabéns! Você acertou em {tentativas} tentativas!")
                break

        except ValueError:
            print("Entrada inválida. Digite apenas números.")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()

    if jogar_novamente != "s":
        print("Obrigado por jogar, até a próxima!")
        break