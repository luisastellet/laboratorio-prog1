#Alunos: Luisa Muniz Stellet e Samuel Trindade
#Turma: A1

#pedindo ao usuario os dados e criando a lista a partir do split
lista = input('Entre com os elementos da lista: ').split()
#pedindo ao usuario o elemento
elemento = input('Entre com o elemento a ser encontrado: ')
#estamos considerando que o usuário não colocará o mesmo elemento duas vezes
#cria um for que acontece até o final da lista. Precisa checar se o elemento da lista na posi8ção atual ŕe igual ao elemento. SE for igual, a posição recebe o valor i. Nesse processo, entende-se que não haverá mais de um elemento na lista que corresponde ao elemento digitado 
for i in range(len(lista)):
    if lista[i] == elemento:
        posicao = i
#printando a saída pedida
print('O elemento', elemento, 'está na posição', posicao)