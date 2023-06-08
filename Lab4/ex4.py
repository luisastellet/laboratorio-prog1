#Alunos: Luisa Muniz Stellet e Samuel Trindade
#Turma: A1

#pedindo para o usuário escrever a frase e deixando tudo minúsculo para realizar a análise
frase = input("Entre com a frase: ").lower()
#pedindo ao usuário escrever a chave e deixando tudo minúsculo para realizar a análise
chave = input("Entre com a chave: ").lower()
#criando a variável frasefinal para guardar a frase original
frasefinal = ""
#todas as letras do alfabeto serão usadas como chave se não for fonecida uma chave
if chave == "":
    chave = "abcdefghijklmnopqrstuvwxyz"
#o for mais externo percorre letra por letra da frase, para que seja analisada 
for letra_frase in frase:
# iniciando essa variável na posição 0, para que seja a primeira letra da frase
    posicao = 0
#analisando quando a posição da -1, quando chega a ultima letra da frase, já que não possui espaço branco entre ela.
    if chave.find(letra_frase) != -1:
        #o for interno percorre a chave, analisando cada letra da chave até chegar ao final dela
        for letra_chave in chave:
            #se a letra da frase da vez for igual à letra da chave da vez, a letra da frase precisa ser aletarada então. Na frasefinal, será colocada a letra pertencente à chave que corresponde à posição do tamanho da chave menos a posição atual mais um(já que as posições começam em 0) 
            if letra_chave == letra_frase:
                frasefinal = frasefinal + chave[len(chave) - (posicao+1)] #[len(chave) - (posicao+1)] indica o elemento oposto
            #a posição deve ser incrementada em 1 para seguir para a próxima rodada do for
            posicao += 1
#Se for -1,ou seja, não há mais espaços em branco, a análise não deve ser feita. Nesse cado, apenas adiciona-se à frasefinal a letra da frase origianl, sem trocá-la
    else:
        frasefinal = frasefinal + letra_frase
#imprimir a frase final
print("Frase codificada: " + frasefinal)