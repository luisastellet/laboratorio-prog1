#Alunos: Luisa Muniz Stellet e Samuel Trindade
#Turma: A1

#Pedindo ao usuário um input e já transformando em lista pelo split()
lista = input('Entre com uma lista: ').split()
#pedindo ao usuário o elemento
elemento = input('Entre com um elemento para se verificar o número de vezes que ele aparece na lista: ')
#iniciando o contador
cont = 0
#comparando se a string da loista na posição atual é igual ao elemento. Se forem iguais, o contador incrementa 1. Esse processo ocorre até o final da lista, por isso o uso do for
for i in range (len(lista)):
    if lista[i] == elemento:
        cont += 1
#Printando o resultado, o contador
print('O elemento', elemento, 'aparece', cont, 'vezes na lista.')