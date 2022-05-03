#A função open() é utilizada para a abertura dos arquivos.
#Sua sintaxe é:
#arquivo = open(‘arquivo.txt’, ‘w’)

#Ao utilizar ‘w’ em um arquivo já existente, ele reescreverá 
# todo o conteúdo do arquivo, fazendo com que todos 
# os dados que estavam nele sejam apagados.


#Função write()
#A função write() é utilizada para gravar
#informações em um arquivo existente.

#Sua síntaxe é:
#arquivo.write (‘Curso Python n’)
#arquivo.write (‘Aula Prática’)

#Na função, adicionamos o nome do arquivo e, logo após o símbolo 
# do ponto final, fazemos a chamada da função write. Em seguida, 
# adicionamos o texto que deverá ser gravado entre aspas simples.



#Função close()

#A função close() é muito importante para encerrar
#  o arquivo após sua utilização.

#Atenção: Nunca abra o arquivo com a função open e
# depois o faça de novo, sem antes fechar a instância 
# anterior.

#Sua síntaxe é:

#arquivo.close()


#GRAVAR.PY
arquivo = open('arqText.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula Pratica \n')
arquivo.write('r :	Abre o arquivo somente para leitura.O arquivo deve já existir. \n')
arquivo.write('r+ :	Abre o arquivo para leitura e escrita. O arquivo deve já existir.\n A escrita começa a partir da primeira linha e, caso exista algo escrito no arquivo, as linhas serão reescritas, conforme formos escrevendo. \n')
arquivo.write('w :	Abre o arquivo somente para escrita, no início do arquivo.\n Apagará o conteúdo do arquivo se ele já existir. Criará um arquivo novo se não existir. \n')
arquivo.write('w+ : Abre o arquivo para escrita e leitura, apagando o conteúdo preexistente.\n')
arquivo.write('a : Abre o arquivo para escrita no final do arquivo. Não apaga o conteúdo preexistente \n')
arquivo.write('a+ : Abre o arquivo para escrita no final do arquivo e leitura')
arquivo.close()

#Função read()
#A função read() realiza a leitura
# de todo conteúdo do arquivo.

#Sua sintaxe é:

#leitura=open(‘arquivo.txt, ‘r’)
#print leitura.read()
#leitura.close()

#Utilizamos o parâmetro ‘r’ que representa que o arquivo
#  está sendo aberto em modo leitura.

leitura=open('arqText.txt', 'r')
print(leitura.read())
leitura.close