#Julia Ribeiro, Maria Lúcia Cecim e Luisa Muniz Stellet
#Turma A1

#criando a função
def tabuleiro (matriz, numero):
    #assumindo que toda fileira terá o mesmo número de cadeiras, por ser um cinema e todos os exemplos dados mostram isso
    casos = 0
    #criando um for para percorrer todas as linhas da matriz
    for i in range(len(matriz)):
        #criando um for para analisar cada poltrona
        for x in range(len(matriz[i])-numero+1):
            verificador = True
            #um for interno que analisa a quantidade de cadeiras correspondendo ao numero pedido
            for y in range(numero):
                if matriz[i][x+y] != 0:
                    verificador = False
            #se ocorrer um caso em que caibam as pessoas juntas, o contador de casos aumenta 1
            if verificador == True:
                casos += 1
    return casos

print(tabuleiro([
[1, 0, 1, 0, 1, 0, 1],
[0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 1, 1, 1, 1],
[1, 0, 1, 1, 0, 0, 1],
[1, 1, 1, 0, 1, 0, 1],
[0, 1, 1, 1, 1, 0, 0]
], 2))

print(tabuleiro([
[1, 0, 1, 0, 1, 0, 1],
[0, 1, 0, 0, 0, 0, 0],
], 4))

