# -*- coding: utf-8 -*-
import random
import string

tamanho_arquivo = 5800
letras = string.ascii_uppercase
digitos = string.digits

# Formatação Arquivo Boleto: 3D-3L-6D-2S-1L-DATA-4S-2L-32D

with open('boletos-importacao.txt', 'w') as boletos:
    info_boleto = ""
    for linha in range(tamanho_arquivo):
        info_boleto += "".join([random.choice(digitos) for x in range(3)])
        info_boleto += " - - "
        info_boleto = "".join([random.choice(letras) for x in range(3)])
        info_boleto += "".join([random.choice(digitos) for x in range(6)])
        info_boleto += "  "
        info_boleto += "".join([random.choice(letras) for x in range(1)])
        info_boleto += str(random.randint(10, 21)) + "112022"
        info_boleto += "    "
        info_boleto += "".join([random.choice(letras) for x in range(2)])
        info_boleto += "".join([random.choice(digitos) for x in range(32)])
        info_boleto += "\n"
        boletos.write(info_boleto)