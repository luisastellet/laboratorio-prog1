entrada = input().split()
lista = []
for c in range(0, len(entrada), 1):
    lista.append(int(entrada[c]))
pares = 0
for i in range(0, len(entrada)-1, 1):
    cont = 1
    if lista.index(lista[i]) == i:
        for j in range(i+1, len(entrada), 1):
            if entrada[j] == entrada[i]:
                cont += 1
        pares += cont // 2
print(f"Lista de meias = {lista}")
print(f"{pares} pares")
