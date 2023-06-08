#Alunos: Luisa Muniz Stellet e Júlia Ribeiro Staudohar
#Turma: A1
#Laboratório 3

#Iniciando a variável opcao
opcao = "S"
#Enquanto a variável opcao for = "S" aparece a pergunta para ele decidir se quer entrar com um número
while opcao == "S":
    opcao = input("Deseja entrar com um número (S/N)? ")
#Se o usuário digitar "S", é pedido um número
    if opcao == "S":
        num = int(input("Entre com o número: "))
        print("Divisores de", num,":")
#Inicia-se a variável numero_divisores
        numero_divisores = 0
        divisor = 1
        
#Analisa-se os divisores: Esse processo se repete até que o valor da variável divisor seja menor ou igual ao número
        while divisor <= num:
            #Se o número dividido por outro tiver resto 0, é porque eles tem uma relação de divisibilidade
            if num % divisor == 0:
                print(divisor)
                numero_divisores = numero_divisores + 1
            divisor = divisor + 1
        #Se ao final das divisões o número só tiver dois divisores, ele será primo
        if numero_divisores == 2:
            print("Número é primo")

        