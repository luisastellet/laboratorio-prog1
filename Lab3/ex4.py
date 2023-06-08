#Alunos: Luisa Muniz Stellet e Júlia Ribeiro Staudohar
#Turma: A1
#Laboratório 3

#Pedindo ao usuário o valor final da tabela de multiplicação
numero = int(input("Entre com o número final da tabela de multiplicação: "))
#Estabelescendo valores iniciais para as parcelas
primeira_parcela = 1
segunda_parcela = 0
#A repetição deve ocorrer a quantidade de vezes inserida pelo usuário e a cada rodada deve acrescentar 1 à primeira parcela e reiniciar a segunda parcela com 0 (nesse for a preocupação é com a primeira parcela)
for i in range(numero):
    for c in range(numero):
        #Dentro da repetição externa, ocorre outra repetição com a quantidade de vezes do número inserido, acrescentando 1 à segunda_parcela e calculando o resultado que é a multiplicação da primeira_parcela com a segunda_parcela (nesse for a preocupação é com a segunda parcela)
        segunda_parcela = segunda_parcela + 1
        resultado = primeira_parcela * segunda_parcela
        print(primeira_parcela, "x", segunda_parcela, "=", resultado)
   
    primeira_parcela = primeira_parcela + 1
    segunda_parcela = 0

# primeira_parcela * segunda_parcela = resultado