import math as mt

def delta(a,b, c):
   delta = mt.pow(b,2) - 4 * a * c
   return delta

def raizes(delta, a, b):
   raiz1 = (- b + mt.sqrt(delta)) / (2 * a)
   raiz2 = (- b - mt.sqrt(delta)) / (2 * a)
   saida = f"Raiz 1 ={raiz1:2f}\nRaiz 2 ={raiz2:.2f}"
   return saida
try:

   #Entrada de dados
   print("Aplicativo para calcular as raizes de uma equação do 2°--")
   a = float (input("digite o valor de a: "))
   b = float (input("digite o valor de b: "))
   c = float (input("digite o valor de c: "))
   print(f"Equação -> {a}x² + {b}x + {c} = 0")


   #Processamento de dados
   delta1 = delta(a, b, c)
   if delta1 < 0: 
      print ("Raízes impossiveis")
   else: 
    dados = raizes(delta1, a, b)

       #Saída de dados

    print(f"As raizes da equação de segundo grau são:\n\t{dados}")
except ValueError: 
   print("Digite um valor valido")

except ZeroDivisionError:
   print("Digite um valor valido") 
      
