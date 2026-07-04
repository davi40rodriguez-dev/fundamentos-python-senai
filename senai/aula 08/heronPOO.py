import principal as t

#Instruções dos objetos da classe triangulo
trianguloX = t.Triangulo()
trianguloY = t.Triangulo()
LADOA = "Lado a ="
LADOB = "Lado b ="
LADOC = "Lado c ="

#Entrada de dados
print("Digite as medidas do triangulo X:")
trianguloX.lado_A = float(input(LADOA ))
trianguloX.lado_B  = float(input(LADOB))
trianguloX.lado_C = float(input(LADOC))

print("Digite as medidas do triangulo Y:")
trianguloY.lado_A  = float(input(LADOA ))
trianguloY.lado_B = float(input(LADOB))
trianguloY.lado_C = float(input(LADOC))

#Saída de dados
print(f"Área do triângulo X: {trianguloX.area:.4f}")
print(f"Área do triângulo Y: {trianguloY.area:.4f}")