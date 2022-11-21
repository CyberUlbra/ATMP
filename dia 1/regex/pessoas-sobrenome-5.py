import re

pessoas = []
regex = "\s[a-z]{5}$"

with open('pagamentos-exemplo.csv', 'r') as csv:
    linhas = csv.readlines()

    for linha in linhas[1:]:
        conteudo = linha.split(',')
        pessoa = conteudo[1]
        if re.findall(regex, pessoa):
            pessoas.append({"nome": pessoa, "salario": "R$ {}".format(conteudo[-1])})

print(pessoas)