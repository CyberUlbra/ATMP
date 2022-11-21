import re

regex = '[199]{4}'
doc_linhas = []

with open('pagamentos-exemplo.csv', 'rw') as csv:
    linhas = csv.readlines()
    
    for linha in linhas:
        linha = re.sub(regex, "2022", linha)
        doc_linhas.append(linha)

    with open('pagamentos-corrigidos.csv', 'w') as csv_corrigido:
        csv_corrigido.writelines(doc_linhas)