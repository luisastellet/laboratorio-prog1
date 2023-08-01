#Julia Ribeiro, Maria Lúcia Cecim e Luisa Muniz Stellet
#Turma A1

#criando a função
def pitagorica(lista):
    #bubble sort para acharmos a hipotenusa, já que será o último elemento da lista, lista[2]
    for x in range(len(lista)):
        for y in range(len(lista) -1 - x):
            if lista[y] > lista[y+1]:
                prov = lista[y]
                #trocando a posição mais a esquerda pelo menor valor
                lista[y] = lista[y+1]
                #trocando a posição mais a direita pelo valor da provisoria (maior)
                lista[y+1] = prov

    #vendo se é pitagórico pela fórmula dada
    if (lista[0] ** 2) + (lista[1] ** 2) == (lista[2] ** 2):
        resposta = True
    #se não seguir a fórmula, a resposta é false
    else:
        resposta = False

    #comparando as duplas
    primitivo = True
    #fazendo um for externo que fixa cada elemento da lista até o penultimo
    for i in range(len(lista)-1):
        divisor = lista[i] #menor entre os dois pois está ordenado
        divisores1 = 0 #precisam ser diferentes para entrar no while
        divisores2 = 1
        #um for mais interno que vai do seguinte ao fixado na posição i até o final da lista
        for j in range(i+1, len(lista)):
            #enquanto os divisores forem diferentes, continua para achar o máximo divisor comum
            while divisores1 != divisores2: #quando for igual, achamos o maior divisor comum
                #se o elemento da lista fixado for divisivel pelo divisor, divisores1 recebe o valor do divisor
                if lista[i] % divisor == 0:
                    divisores1 = divisor
                #se o elemento da lista na posição j for divisivel pelo divisor, divisores2 recebe o valor do divisor
                if lista[j] % divisor == 0:
                    divisores2 = divisor
                #se os divisores1 e 2 forem diferentes, a variavel divisor descresce em 1
                if divisores1 != divisores2: #quando acabar o processo, não subtrair 1 do divisor por isso prefira do if
                    divisor -= 1 
            #depois de analisar o primeiro da lista com todo os outros números, se o divisor1 for diferente de 1, o primitivo é False. Lembrando que nesse momento divisores1 e 2 são iguais, já que saiu do while
            if divisores1 != 1:
                primitivo = False
    
    #analisando as respostas, juntando o pitagorico com o primitivo
    if resposta == True and primitivo == True:
        return True
    else: #quando pelo menos um for False, precisa imprimir False
        return False

#usamos para testar as funções, iguais aos exemplos dados
print(pitagorica([4, 5, 3]))
print(pitagorica([7, 12, 13]))
print(pitagorica([39, 15, 36]))
print(pitagorica([77, 36, 85]))