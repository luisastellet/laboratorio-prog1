# Alunos: Luisa Muniz Stellet e Samuel Trindade
# Turma: A1

#Solicitando ao usuário a variável A
A = int(input("Entre com o valor de A:"))
#Solicitando ao usuário a variável B
B = int(input("Entre com o valor de B:"))
#Solicitando ao usuário a variável C
C = int(input("Entre com o valor de C:"))
#Solicitando ao usuário a variável D
D = int(input("Entre com o valor de D:"))

#Criando uma condição para tudo o que foi solicitado no exercício. Se seguir os requisitos, imprime "valores aceitos", senão imprime "valores não aceitos"
if B > C and D > A and C+D > A+B and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos.")
else:
    print("Valores não aceitos.")