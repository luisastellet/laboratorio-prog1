# Exercício 3 - Julia Staudohar, Luisa Stellet e Maria Lúcia Cecim

#iniciando a lista inserida pelo usuário
dados = int(input("Entre com a quantidade de dados: "))
#criando a listade ident e freq para guardamos os dados
ident = []
freq = []
#inicializando o contador de frequencias
freqtotal = 0
#criando um forpara receber as entradas de acordo com o numero de dados
for i in range(dados):
    #colocando na lista ident o identificador atual
    ident.append(input(f"Entre com o identificador do dado {i+1}: "))
    #colocando na lista freq a frequencia atual
    freq.append(int(input(f"Entre com a frequência do dado {ident[i]}: ")))
    #incluindo ao contador freqtotal a frequencia atual
    freqtotal += freq[i]
#criando um for para imprimir as respostas de acordo com a quantidade de dados
for j in range(dados):
    #calculando as frequencias
    resultado = freq[j] * (360 / (freqtotal))
    #imprimindo o resultado
    print(f'["{ident[j]}": {int(resultado)}]')