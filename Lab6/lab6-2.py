# Exercício 2 - Julia Staudohar, Luisa Stellet e Maria Lúcia Cecim

#dados de entrada
dados = input().split()
entrada = []
for i in range(len(dados)):
    entrada.append(int(dados[i]))
#criando lista vazia - lucros
lucros = []
#percorrendo a lista de entrada e verificando se ocorre lucro, caso ocorra é adicionado a lista lucros
for i in range(len(entrada)):
    for j in range(i+1, len(entrada)):
        if entrada[j] > entrada[i]:
            lucro = entrada[j] - entrada[i]
            lucros.append(lucro)
#variável do lucro para imprimir, caso não ocorra irá imprimir -1
menor = -1
for k in range(len(lucros)):
    if lucros[k] > menor:
        menor = lucros[k]
#imprimindo saída
print('Lucro máximo é', menor)