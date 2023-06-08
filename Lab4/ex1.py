#Alunos: Luisa Muniz Stellet e Samuel Trindade
#Turma: A1

suporte = "0123456789"
#pedindo ao usuário o número
numero = int(input("Entre com um número inteiro positivo: "))
#registando o resultado final
resultado = ""
#enquanto o número for maior que 0, faça:
while numero > 0:
    #o resultado vai receber o suporte com o valor do resto da divisão do número por 10 mais o resultado que já estava guardado na variável, para interligar o número do usuário com a string suporte á cadastrada
    resultado = suporte[numero % 10] + resultado
    #o novo número será o anterior divido de forma inteira por 10, para que o while continue rodando
    numero = numero // 10    

#printar o resultado após o while terminar
print("O número foi atribuído à variável do tipo 'string' e tem o valor “"+ resultado +"”")