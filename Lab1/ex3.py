# Alunos: Luisa Muniz Stellet e Samuel Trindade
# Turma: A1

#Atribuindo à variável velocidade o valor informado pelo problema
velocidade = 340

#Pedindo para o usuário informar o tempo
tempo = float(input("Entre com o tempo (em segundos) transcorrido entre ver o raio e ouvir o trovão: "))

#Calculando a distância 
distancia = velocidade * tempo

#Imprimindo para o usuário a distância que o raio caiu
print("Como o tempo de ouvir o trovão foi de", tempo, "segundo, o raio caiu a", distancia, "metros daqui.")
