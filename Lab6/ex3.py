quantidade = int(input("Entre com a quantidade de dados: "))
ident = []
freq = []
for i in range(quantidade):
    ident.append(input(f"Entre com o identificador do dado {i+1}: "))
    freq.append(int(input(f"Entre com a frequência do dado {ident[i]}: ")))
freqtotal = 0
for j in range(len(freq)):
    freqtotal += freq[j]
for c in range(len(freq)):
    print(f'["{ident[c]}": {freq[c] * (360 / freqtotal):.0f}]')