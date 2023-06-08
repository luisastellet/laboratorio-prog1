#Alunos: Luisa Muniz Stellet e Júlia Ribeiro Staudohar
#Turma: A1
#Laboratório 3

#Inicializando a variável soma e contador de valores positivos
soma = 0
contador = 0
#A repetição deve ocorrer 6 vezes, pedindo ao usuário 6 valores diferentes
for c in range(6):
    num = float(input("Entre com um valor: "))
    #Se o número for maior que 0, positivo, ele deve ser incluído na soma, e soma-se 1 ao contador
    if num > 0:
        soma = soma + num
        contador += 1

#Ao final das repetições, a média será calculada pela soma dividida pelo contador de números positivos
media = soma / contador
#Imprimir a quantidade de valores positivos e a média deles
print(contador, "valores positivos")
print(media)