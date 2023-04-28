# Alunos: Luisa Muniz Stellet e Samuel Trindade
# Turma: A1

#Importando a biblioteca math
import math

#Pedindo as coordenadas do ponto A
Xa = float(input("Entre com a coordenada x do ponto A:"))
Ya = float(input("Entre com a coordenada y do ponto A:"))

#Pedindo as coordenadas do ponto B
Xb = float(input("Entre com a coordenada x do ponto B:"))
Yb = float(input("Entre com a coordenada y do ponto B:"))

#Pedindo as coordenadas do ponto C
Xc = float(input("Entre com a coordenada x do ponto C:"))
Yc = float(input("Entre com a coordenada y do ponto C:"))

#Usando a fórmula matemática da distância entre dois pontos para calcular os lados do possível triângulo
Lado1 = math.sqrt((Xb - Xa)**2 + (Yb - Ya)**2)
Lado2 = math.sqrt((Xc - Xb)**2 + (Yc - Yb)**2) 
Lado3 = math.sqrt((Xa - Xc)**2 + (Ya - Yc)**2)

#Criando a condição para ser triângulo: A soma de dois lados distintos precisa ser maior que o terceiro lado
if Lado1 + Lado2 > Lado3 or Lado1 + Lado3 > Lado2 or Lado2 + Lado3 > Lado1:
    
    #Já sendo um triângulo, analisa-se os lados para classificá-lo quanto ao tipo
    if Lado1 == Lado2 == Lado3:
        print("Equilátero")
    elif Lado1 == Lado2 or Lado1 == Lado3 or Lado2 == Lado3:
        print("Isósceles")
    else:
        print("Escaleno")
