SENHA = 2002
contagem = 0
#Entrada de dados
senha = int(input('Digite a senha: '))
while (senha !=SENHA):
    contagem += 1
#FAÇA O LOOP
    senha = int(input('Senha invalida, tente novamente: '))
    if (contagem >= 3):
        print("Número de tentativas excedido")
    break
if contagem <= 2:
    print('Acesso permitido!')
else:
    print("Acesso permitido!")