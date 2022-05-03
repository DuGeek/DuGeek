fruta = input("Digite o nome de uma fruta: ")
#Quando utilizamos a entrada de dados por meio da função input, essa será considerada do tipo string.
# Assim, caso seja necessário realizar a entrada de valores numéricos, temos de converter o tipo de dado, 
# de acordo com o tipo que desejamos armazenar na variável.
codigo = int(input("Digite o código do funcionário: "))
nome = input("Digite o nome do funcionário: ")
salario = float(input("informe o salario: "))
ativo = true

print("Código: %d "% codigo)
print("Nome: %.s "% nome)
print("Salário: %"% salario)
print("Ativo: %"% ativo)