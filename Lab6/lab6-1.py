# Exercício 1 - Julia Staudohar, Luisa Stellet e Maria Lúcia Cecim

#iniciando a lista dos valores
entrada = input().split()
#criando a lista para serem adicionados os inteiros
lista = []
#iniciando o contador de pares
pares = 0

#criando um for para apendar os valores da entrada na lista, tranformando tudo em inteiro
for c in range(0, len(entrada), 1):
    lista.append(int(entrada[c]))

#criando um contador externo que vai até o úlimo 
for i in range(0, len(entrada)-1, 1):
    #contador de meias inicia em 1 já que o atual não foi contado ainda
    cont = 1
    #se for a primeira aparição desse núero, faça a análise
    if lista.index(lista[i]) == i:
        #um for de dentro para comparar a meia "fixada" no for externo com as próximas
        for j in range(i+1, len(entrada), 1):
            #se a "fixada" for igual a ataual, aumenta 1 no contador
            if entrada[j] == entrada[i]:
                cont += 1
        #depois de analisar a primeira com todas, realiza a divisão inteira por 2 para descobrir o numero de pares
        pares += cont // 2
#printar a lista de meias
print(f"Lista de meias = {lista}")
#printar o numero de pares
print(f"{pares} pares")