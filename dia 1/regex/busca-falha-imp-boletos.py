# -*- coding: utf-8 -*-
import re

linhas_com_erro = []
regex = "[a-zA-z]{3}[0-9]{6}\s{2}[a-zA-z][0-9]{8}\s{4}[a-zA-z]{2}[0-9]{32}"

with open('boletos-importacao.txt', 'r') as importacao:
    linhas = importacao.readlines()
    [linhas_com_erro.append(linhas.index(x)+1) for x in linhas if not re.findall(regex, x)]

print("Posições com erro: {}".format(linhas_com_erro))
