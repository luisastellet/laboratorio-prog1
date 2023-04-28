# Alunos: Luisa Muniz Stellet e Samuel Trindade
# Turma: A1

#Pedindo ao usuário para entrar com o valor
valor = float(input("Entre com um número real:"))

#Criando a condição para o intervalo [0,25]
if 0 <= valor <= 25:
    print("Intervalo [0,25]")
    
#Criando a condição para o intervalo (25,50]
elif 25 < valor <= 50:
    print("Intervalo (25,50]")
    
#Criando a condição para o intervalo (50,75]
elif 50 < valor <= 75:
    print("Intervalo (50,75]")

#Criando a condição para o intervalo (75,100]
elif 75 < valor <= 100:
    print("Intervalo (75,100]")
    
#Criando a condição para valores fora dos intervalos solicitados no exercício
else:
    print("Fora de intervalo")     