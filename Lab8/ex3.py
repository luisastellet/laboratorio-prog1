#Laboratório 8
#Alunos: Julia Staudohar, Luisa Stellet e Maria Lúcia Cecim

#criando a função letras_agrupadas
def letras_agrupadas(nomearquivo, quantidade):
    #abrindo o arquivo e ativando o moto write
    arquivo = open(nomearquivo, 'w')
    #criando um auxiliar com as letras do alfabeto
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #criando um for que usa o incremento de quantidade, para o i ir mudando baseado nisso
    for i in range(0, 27, quantidade):
        #escrevendo no arquivo o que tem no alfabeto da posição i até i+quantidade considerando que o slice tira 1
        arquivo.write(alfabeto[i:i+quantidade])  
        #pulando as linhas
        arquivo.write('\n')
    #fechando o arquivo
    arquivo.close()
letras_agrupadas('alfabeto.txt', 3)