#Laboratório 8
#Alunos: Julia Staudohar, Luisa Stellet e Maria Lúcia Cecim

#criando a função
def vencedores(nomearquivo, arquivosaida):
    #abrindo o arquivo de leitura
    arquivo = open(nomearquivo, 'r')
    #abrindo o arquivo de escrita
    saida = open(arquivosaida, 'w')
    #iniciando a matriz
    matriz = []
    #appendando na matriz as informações dos países
    for i in arquivo:
        matriz.append(i.split())
    #criando dois fors aninhandos para ordenarem a matriz, linha por linha, lembrando que queremos a ordem descrescente
    for j in range(len(matriz)-1):
        for c in range(len(matriz)-1):
            #se as medalhas de ouro da linha de cima for menor que a quantidade da linha de baixo, o aux recebe a linha de baixo, a de baixo recebe o valor da linha de cima e a linha de cima recebe o aux
            if int(matriz[c][1]) < int(matriz[c+1][1]):
                aux = matriz[c+1]
                matriz[c+1] = matriz[c]
                matriz[c] = aux
    #criando um for para ajustar as respostas, tranformando as listas em string para escrever no arquivo
    for z in range(len(matriz)):
        resp = ''
        for x in range(len(matriz[z])):
            resp += str(matriz[z][x]) + ' '
        #escrevendo no arquivo os dados dos países na ordem certa
        saida.write(resp.strip())
        #pulando linha
        saida.write('\n')
    #fechando os
    arquivo.close()
    saida.close()

vencedores('olimpiada.txt','vencedor.txt')
