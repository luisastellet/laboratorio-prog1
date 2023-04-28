# Alunos: Luisa Muniz Stellet e Samuel Trindade
# Turma: A1

#Solicitando ao usuário o número do funcionário
funcionario = int(input("Entre com o número do funcionário: "))

#Solicitando ao usuário o número de horas trabalhadas
horas = int(input("Entre com  quantidade de horas trabalhadas: "))

#Solicitando ao usuário o valor da hora trabalhada
valor_hora = float(input("Entre com o valor da hora trabalhada: "))

#Cálculo do salário recebido pelo funcionário (horas trabalhadas vezes o valor da hora trabalhada)
salario = horas * valor_hora

#Mostrar ao usuário o seu salário
print("O funcionário de número", funcionario, "deve receber R$", salario)