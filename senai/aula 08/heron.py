LADOA = "Lado a ="
LADOB = "Lado b ="
LADOC = "Lado c ="

#Entrada de dados
print("Digite as medidas do triangulo X:")
ax = float(input(LADOA ))
bx = float(input(LADOB))
cx = float(input(LADOC))

print("Digite as medidas do triangulo Y:")
ay = float(input(LADOA ))
by = float(input(LADOB))
cy = float(input(LADOC))

#Processamento de dados
px = (ax + bx + cx) / 2
py = (ay + by + cy) / 2
areax = (px * (py - ay) * (px - bx) * (px - cx))**0.5
areay = (py * (py - ay) * (px - bx) * (px - cx))**0.5

#Saída de dados
print(f"Área do triângulo X: {area:.4f}")
print(f"Área do triângulo Y: {area:.4f}")