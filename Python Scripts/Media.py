nota1=float(input("Informe a primeira nota: "))
nota2=float(input("Informe a segunda nota: "))

#calcular media
mediafinal = (nota1 + nota2) / 2 

#verificaçao
if mediafinal >=7.0:
    print("A Média: %1f - Aprovado " % mediafinal)
else:
    print("A Média: %.1f - Reprovado " % mediafinal)


#Adicionalmente, se existir mais de uma condição alternativa 
# que precise ser verificada, utilizamos a condição elif, 
# pois ela avalia as expressões intermediárias antes do
#  comando else.

idade = int(input("Digite a idade:"))
if idade > 18:
    print("Maior Idade")
elif idade > 16:
    print("Infanto juvenil")
else:
    print("Menor Idade")