#Alunos: Luisa Muniz Stellet e Samuel Trindade
#Turma: A1

#pedindo ao usuário a lista, criada a partir do split
lista0 = input('Entre com os elementos da lista: ').split()
#pedindo ao usuario a posição
posicao = int(input('Entre com a posição do elemento a ser retirado: '))
#inicializando a lista1
lista1 = []
#criando um for para adicionar à lista1 os elementos da posição atual da lista0.
for i in range(posicao):
   lista1.append(lista0[i])
#igualando lista2 a lista1
lista2 = lista1
#incluindo na lista final(lista2) os elementos que sobraram, que estão na lista0 a partir da posição+1
for c in range(posicao+1, len(lista0)):
   lista2.append(lista0[c])
#precisamos ajustar a resposta para string, por isso criar a string vazia
resposta = ''
#criar um for para adicionar à string(resposta) cada elemento da lista2 na posição atual(j), a lista final, até o len da lista2
for j in range(len(lista2)):
   resposta += lista2[j] + ' '
#printar a resposta 
print('Lista:', resposta)  