#Julia Ribeiro, Maria Lúcia Cecim e Luisa Muniz Stellet
#Turma A1

#iniciando a função
def fatorial (numero):
    #iniciando o resto para entrar no while
    resto=1
    #o fator do fatorial começa em 1
    fator=1
    #valor é o resultado do fatorial que a cada processo é ele mesmo vezes o fator já que é acumulativo e começa em 1 porque é o valor neutro da multiplicação
    valor = 1
    while resto!=0:
        #calculando quando vale o fatorial atual
        valor*=fator
        #se o resultado do fatorial for divisível peo numero digitado, a resposta é o fator
        if valor%numero==0:
            resposta=fator
            #e o resto passa a ser 0 para que o while pare de funcionar
            resto=0
        #o fator vai sendo incrementado em 1 a cada rodada
        fator+=1
    #retornar a resposta
    return resposta

#testando a função
n= int(input("Digite um número: "))
x=fatorial(n)
print(x)
