import base64

# Criptografando senha
nova_senha = input('Nova senha: ').encode()
bytes64_nova_senha = base64.b64encode(nova_senha)
base64_nova_senha = bytes64_nova_senha.decode()

lista_arquivo = []

# Lendo arquivo
arquivo = open('.exten', 'r')
lista_arquivo = arquivo.readlines()
arquivo.close()

# Escrevendo no arquivo
arquivo = open('.exten', 'w')
lista_arquivo[3]='auth="{}"\n'.format(base64_nova_senha)
arquivo.writelines(lista_arquivo)
arquivo.close()