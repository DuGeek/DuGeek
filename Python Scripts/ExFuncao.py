#>>1.def
#A palavra def determina o início da função.


#>>2. Parâmetros
#São informações que a função pode receber para o seu processamento.
#Os parâmetros podem existir ou não.

#>>3. Corpo da função
#É o local em que é aplicada a sequência de instruções, como entrada,
# processamento e/ou saída.

#>>4. return
#Deve ser utilizado quando houver necessidade de retornar alguma 
# informação para a ação da função.

#>>5. Indentação
#Deve possuir quatro espaços em branco e pular duas linhas para o próximo 
# bloco de instruções (próxima função ou programação principal).



def lernotas():
    n=float(input("Digite uma nota para o aluno"))
    return n


def resultado(n1,n2):
    media = (n1+n2) / 2
    print("Nota 1:", n1)
    print("Nota 2:", n2)
    print("Media", media, "Resultado: ")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

a = lernotas()
b = lernotas()
resultado(a,b)