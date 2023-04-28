# Alunos: Luisa Muniz Stellet e Samuel Trindade
# Turma: A1

#Pedindo para o usuário digitar o número de centavos
centavos = int(input("Entre com o valor em centavos: "))

#Criando a variável início para fixar o valor de centavos inicial
inicio = centavos

#Para descobrir quantas moedas de um real seriam necessárias, fizemos uma divisão inteira do valor de centavos inicial por 100 (valor em centavos). Depois disso, atualizamos o valor da varíavel centavos para a quantidade anterior menos a parte inteira vezes o valor da moeda (100)
um_real = centavos // 100
centavos = centavos - (um_real * 100) 

#Para descobrir quantas moedas de cinquenta centavos seriam necessárias, fizemos uma divisão inteira do valor de centavos atual por 50. Depois disso, atualizamos o valor da varíavel centavos para a quantidade anterior menos a parte inteira vezes o valor da moeda (50)
cinquenta = centavos // 50
centavos = centavos - (cinquenta * 50)

#Para descobrir quantas moedas de vinte e cinco centavos seriam necessárias, fizemos uma divisão inteira do valor de centavos atual por 25. Depois disso, atualizamos o valor da varíavel centavos para a quantidade anterior menos a parte inteira vezes o valor da moeda (25)
vintecinco = centavos // 25
centavos = centavos - (vintecinco * 25)

#Para descobrir quantas moedas de dez centavos seriam necessárias, fizemos uma divisão inteira do valor de centavos atual por 10. Depois disso, atualizamos o valor da varíavel centavos para a quantidade anterior menos a parte inteira vezes o valor da moeda (10)
dez = centavos // 10 
centavos = centavos - (dez * 10)

#Para descobrir quantas moedas de cinco centavos seriam necessárias, fizemos uma divisão inteira do valor de centavos atual por 5. Depois disso, atualizamos o valor da varíavel centavos para a quantidade anterior menos a parte inteira vezes o valor da moeda (5)
cinco = centavos // 5
centavos = centavos - (cinco * 5)

#Para descobrir quantas moedas de um centavo seriam necessárias, fizemos uma divisão inteira do valor de centavos atual por 1. Depois disso, atualizamos o valor da varíavel centavos para a quantidade anterior menos a parte inteira vezes o valor da moeda (1)
um = centavos // 1
centavos = centavos - (um * 1)

print("Para o valor", inicio, "centavos, a menor quantidade de moedas é:")
print(um_real, "moeda(s) de 1 real,")
print(cinquenta, "moeda(s) de 50 centavos,")
print(vintecinco, "moeda(s) de 25 centavos,")
print(dez, "moeda(s) de 10 centavos,")
print(cinco, "moeda(s) de 5 centavos e,")
print(um, "moeda(s) de 1 centavos.")