#Alunos: Luisa Muniz Stellet e Samuel Trindade
#Turma: A1

#criando a lista inicial (lista0)
lista0 = input('Entre com os elementos da lista: ').split()
#iniciando a lista1 vazia, que terá os valores até a posição digitada pelo usuário
lista1 = []
#pedindo ao usuário o elemento
elemento = input('Entre com um elemento a ser inserido: ')
#poedindo ao usuário a posição
posicao = int(input('Entre com a posição para inserir o elemento: '))
#utiliza-se um for até um passo antes da posição digitada. Nesse for, acrescenta-se à lista1 o elemento da lista0 na posição atual
for i in range(posicao):
   lista1.append(lista0[i])
#após isso, acrescenta-se à lista1 o elemento desejado
lista1.append(elemento)
#cria a lista2 igual à lista1, que conterá tudo0 até agora mais oa valores que sobraram
lista2 = lista1
#cria um for para incluisr na lista2 os valores da lista0 a partir da posição
for c in range(posicao, len(lista0)):
   lista2.append(lista0[c])
#precisamos ajustar a resposta para string, por isso criar a string vazia
resposta = ''
#criar um for para adicionar à string(resposta) cada elemento da lista2 na posição atual(j), a lista final, até o len da lista2
for j in range(len(lista2)):
   resposta += lista2[j] + ' '
#printar a resposta 
print('Lista:', resposta)  


