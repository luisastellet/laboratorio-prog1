# Alunos: Luisa Muniz Stellet e Samuel Trindade
# Turma: A1

#Importando a biblioteca math
import math 

#Pedindo para o usuário informar o raio em centímetros
raio = float(input("Entre com o raio em centímetros: "))

#Cálculo do perímetro da circunferência utilizando a biblioteca math (2 vezes pi vezes o raio)
perimetro = 2 * math.pi * raio

#informando ao usuário o perímetro da circunferência
print("O perímetro da circunferência de raio", raio, "cm é", perimetro)