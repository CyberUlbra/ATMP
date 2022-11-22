# Criando arquivo
arquivo = open('arquivo.txt', 'a')

# Escrevendo dados
arquivo = open('arquivo.txt', 'a')

arquivo.write('Ola mundo!')
arquivo.close()

# Escrevendo mais dados
arquivo = open('arquivo.txt', 'a', encoding='utf-8')

frases = list()
frases.append("Minicurso \n")
frases.append("Automatizando tarefas maçantes com python \n")
frases.append("Manipulação de arquivos \n")

arquivo.writelines(frases)
arquivo.close()

# Lendo arquivo
arquivo = open('arquivo.txt', 'r', encoding='utf-8')

print(arquivo.read())
arquivo.close()