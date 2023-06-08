#Alunos: Luisa Muniz Stellet e Samuel Trindade
#Turma: A1

#pedindo ao usuário para digitar a frase e já deixando tudo minúsculo
frase = input("Entre com uma frase: ").lower()
#iniciando a variável posição com 0, para analisar a primeira letra da frase
posicao = 0
#criando a variável frasefinal para guardar a frase original
frasefinal = ""
#Enquanto a posição for diferente de -1 faça (a posição será -1 quando já tiver acabado de percorrer a frase toda)
while posicao != -1:
    #inclui na frasefinal a letra da posição 0 maiúscula, ou seja, a primeira letra da frase
    frasefinal += frase[posicao].upper()
    #grava-se a posição atual em uma nova variável para ser retomada depois
    posicaoanterior = posicao
    #a posição atual receberá o valor do primeiro espaço em branco a ser achado, que mostra o fim da primeira palavra
    posicao = frase.find(" ", posicao)
    #precisa analisar o caso em que a posição dá -1, que seria chegndo na última palavra da frase, já que não tem espaço em branco após ela
    if posicao != -1:
        #incrementa pra não analisar o espaço em branco, analisar a próxima letra
        posicao += 1 
        #acrescenta-ase à frasefinal além da primeira letra maiúscula já adicionada na linha 13, o resto da palavra com letras minúsculas
        frasefinal += frase[posicaoanterior+1 : posicao]
    else:
        # se a posição for igual a -1, significa que chegou à última palavra da frase, então acrescenta-se à frasefinal o trecho até o len(frase) que seria a última posição da frase original
        frasefinal += frase[posicaoanterior+1 : len(frase)]
#imprimir a frasefinal já modificada
print(frasefinal)
