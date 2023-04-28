# Alunos: Luisa Muniz Stellet e Samuel Trindade
# Turma: A1

#Pedindo ao usuário para inserir o número
num = int(input("Entre com um número inteiro de 5 dígitos: "))

#Ao dividir o número por 10000, encontra-se o valor que ocupa a dezena de milhar. O resto da divisão do número inicial por 10000 indica o restomilhar, que passará para as próximas divisões
dezenademilhar = num // 10000
restodezenademilhar = num % 10000

#Ao dividir o resto da divisão anterior (o novo número) por 1000, encontra-se o algarismo que ocupa a posição do milhar. O resto da divisão do restodezenademilhar por 1000 indica o restomilhar que passará para as próximas divisões
milhar = restodezenademilhar // 1000
restomilhar = restodezenademilhar % 1000

#Ao dividir o resto da divisão anterior (novo número) por 100, encontra-se o algarismo que ocupa a posição das centenas. Ao pegar o resto da divisão do restomilhar por 100, geramos um novo número para as próximas etapas, o restocentena
centena = restomilhar // 100
restocentena = restomilhar % 100

#Ao dividir o resto da divisão anterior (novo número) por 10, encontra-se o algarismo que ocupa a posição das dezenas. O resto da divisão do restocentena por 10 indica o restodezena.
dezena = restocentena // 10
restodezena = restocentena % 10

#o resto da última divisão indica o novo número, ou seja, o valor que ocupará a casa das unidades
unidade = restodezena

#Se o algarismo do milhar for igual ao algarismo da dezena e o alagrismo da dezena de milhar for igual ao algarismo da unidade, o numero (num) inserido ao início pelo usuário é palíndromo.
if milhar == dezena and dezenademilhar == unidade:
    print("O número é palíndromo.")
