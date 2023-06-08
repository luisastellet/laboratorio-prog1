#Alunos: Luisa Muniz Stellet e Samuel Trindade
#Turma: A1

#criando um suporte, uma string com todas as letras do alfabeto
alfabeto = "abcdefghijklmnopqrstuvwxyz"
#pedindo ao usuário pra entrar com duas palavras na mesma variável
palavras = input("Entre com duas palavras: ")
#criando palavras_min para que cada substring seja analisada individualmente e já com tudo minúsculo
palavras_min = palavras.lower().split()
#guardando as palavras separadas, mas com os caracteres originais para serem printados no final
palavras = palavras.split()
#calculando o tamanho da segunda substring 
tamanho2 = len(palavras[1])
#criando um verificado true que será utilizado posteriormente para verificar a necessidade da realizção de certos passos
verificador = True
# um for que irá percorrer a string alfabeto letra por letra 
for letra in alfabeto:
    #se o verificador for true, aí o pocesso de análise começa
    if verificador == True:
        cont1 = 0 #contador de letras iguais da palavra 1 (posição 0) 
        cont2 = 0 #contador de letras iguais da palavra 2 (posição 1)
        # um for que irá percorrer a primeira substring
        for letra1 in palavras_min[0]:
            #se a letra atual na priemeira substring (letra1) for igual à letra atual do alfabeto (letra), o cont1 aumenta 1 unidade
            if letra == letra1:
                cont1 += 1
        # um for que irá percorrer a segunda substring        
        for letra2 in palavras_min[1]:
            #se a letra atual na segunda substring (letra2) for igual à letra atual do alfabeto (letra), o cont2 aumenta 1 unidade
            if letra == letra2:
                cont2 += 1
        #após percorrer todas as duas substrings, se os contadores forem diferentes, o verificador vira falso
        if cont1 != cont2:
            verificador = False
#no final das análises, se o verificador for true, printa que as palavras são anagramas
if verificador == True:
    print(palavras[0] + " e " + palavras[1] + " são anagramas")
#se o verificador for false, printa que as palavras não são anagramas
else:
    print(palavras[0] + " e " + palavras[1] + " não são anagramas")
