entrada = input().split()
lista = []
maior = 0
for c in range(len(entrada)):
    lista.append(int(entrada[c]))
for i in range(0, len(lista)-1, 1):
    for j in range(i+1, len(lista), 1):
        if lista[i] < lista[j]:
            if lista[j] - lista[i] > maior:
                maior = lista[j] - lista[i]
if maior > 0:              
    print(f"Lista de valores = {lista}")
    print(f"Lucro máximo é {maior}")
else:
    print(f"Lista de valores = {lista}")
    print(f"Lucro máximo é -1")



