#Laboratório 8
#Alunos: Julia Staudohar, Luisa Stellet e Maria Lúcia Cecim

def palavra_repetida(nomearquivo):
    #abrindo o arquivo
    arquivo = open(nomearquivo, 'r')
    #lendo cada linha do arquivo
    palavras = arquivo.readlines()
    #criando um contador para verificar quantas vezes cada palavra aparece
    cont=0
    #criando uma variavel para armazenar a maior quantidade
    maior_cont=0
    #criando lista vazia
    lista=[]
    #adicionando cada palavra em uma lista para verificar
    for i in palavras:
        lista.append(i)
    #comparando quantas vezes aparece cada palavra
    for j in lista:
        cont = lista.count(j)
        #caso a quantidade sej amaior, maior_cont é substituida e a resposta armazena a palavra mais repetida
        if cont > maior_cont:
            maior_cont = cont
            resposta = j
    #fechando o arquivo
    arquivo.close()
    return resposta
print(palavra_repetida('cores.txt'))
