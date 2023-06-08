#Alunos: Luisa Muniz Stellet e Júlia Ribeiro Staudohar
#Turma: A1
#Laboratório 3

#Pedindo ao usuário para entrar com um número
num = int(input("Entre com o número inteiro positivo: "))
#Salvando o valor inicial para ser lido no final
numi = num
#Iniciando contador de dígitos
contador = 0
#Criando uma repetição para enquanto a divisão do número por 10 > 0, acrescenta-se um dígito ao contador
while  num / 10 > 0:
    num = num // 10
    contador = contador + 1
#Imprimir a frase final com o número incial e a quantidade de dígitos
print("O número", numi, "tem", contador, "dígitos")