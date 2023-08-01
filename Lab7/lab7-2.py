#Julia Ribeiro, Maria Lúcia Cecim e Luisa Muniz Stellet
#Turma A1

#iniciando a função com os 3 parametros
def tabuleiro(n, x, y):
    #uma matriz varia para irmos apendando os termos
    matriz = []
    #um for externo para as linhas da matriz
    for i in range(n):
        linha = []
        #um for interno para as colunas da matriz
        for j in range(n):
            #se o indice da linhas for par, ocorrem duas opções:
            if i % 2 == 0:
                #quando o indice que idnica a coluna também for par, apenda o primeiro elemento (x)
                if j % 2 == 0:
                    linha.append(x)
                #se o indice da coluna do elemento for impar, apenda o segundo elemento (y)
                else:
                    linha.append(y)
            #quando o indice da linha for impar, ocorrem duas opções:
            else:
                #se o indice do elemento que indica coluna for par, apenda o segundo eelemento (y)
                if j % 2 == 0:
                    linha.append(y)
                #se o indice do elemento que indica coluna for impar, apenda o primeiro elemento (x)
                else:
                    linha.append(x)
        #depois de organizar cada linha, precisa apendar na matriz
        matriz.append(linha)
    #o retorno é a matriz
    return matriz

#testando o codigo
n = int(input('Digite o tamanho do tabuleiro: '))
x = input('Digite o primeiro elemento: ')
y = input('Digite o segundo elemento: ')
#se os elementos d=forem iguais, printa inválido
if x == y:
    print(f'"Inválido"')
else:
    matriz = tabuleiro(n, x, y)
    #esse for foi criado para a matriz ser impressa linha por linhas
    for i in range(n):
        print(matriz[i])
