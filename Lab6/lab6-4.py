# Exercício 4 - Julia Staudohar, Luisa Stellet, Maria Lúcia Cecim

#entrando com a linha 1 do jogo da velha e transformando em uma lista
linha1 = input().split()
lista1 = []
for i in range(3):
    lista1.append(linha1[i])
#entrando com a linha 2 do jogo da velha e transformando em uma lista
linha2 = input().split()
lista2 = []
for i in range(3):
    lista2.append(linha2[i])
#entrando com a linha 3 do jogo da velha e transformando em uma lista
linha3 = input().split()
lista3 = []
for i in range(3):
    lista3.append(linha3[i])
#verificando linhas do jogo da velha
if lista1[0] == lista1[1] == lista1[2]:
    print(lista1[0], 'é o vencedor.')
elif lista2[0] == lista2[1] == lista2[2]:
    print(lista2[0], 'é o vencedor.')
elif lista3[0] == lista3[1] == lista3[2]:
    print(lista3[0], 'é o vencedor.')
#verificando colunas do jogo da velha
elif lista1[0] == lista2[0] == lista3[0]:
    print(lista1[0], 'é o vencedor.')
elif lista1[1] == lista2[1] == lista3[1]:
    print(lista1[1], 'é o vencedor.')
elif lista1[2] == lista2[2] == lista3[2]:
    print(lista1[0], 'é o vencedor.')
#verificando diagonais do jogo da velha
elif lista1[0] == lista2[1] == lista3[2]:
    print(lista1[0], 'é o vencedor.')
elif lista1[2] == lista2[1] == lista3[0]:
    print(lista1[2], 'é o vencedor.')
else:
    print('Empate')