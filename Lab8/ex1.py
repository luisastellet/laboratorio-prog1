#Laboratório 8
#Alunos: Julia Staudohar, Luisa Stellet e Maria Lúcia Cecim

#inicio da função
def maior_palavra(nomearquivo):
    #abrindo o arquivo txt
    arquivo = open(nomearquivo, 'r')
    #lendo cada linha do arquivo
    palavras = arquivo.readlines()
    #criando um string vazio para ser feita a comparação
    maior = ''
    # cada palavra do arquivo é comparada e substituída na variável maior caso tenha mais letras
    for i in palavras:
        if len(i) > len(maior):
            maior = i
    #fechando o arquivo
    arquivo.close()
    return maior
print(maior_palavra('nomearquivo.txt'))