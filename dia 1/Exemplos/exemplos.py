# Este programa pergunta o seu nome
print('Hello world')
meu_nome = input('Qual é o seu nome: ')

print('Prazer em conhecer você, ' + meu_nome)
print('O tamanho do seu nome é: ' + str(len(meu_nome)))

minha_idade = input('Qual é a sua idade: ')

print('Você vai fazer ' + str(int(minha_idade) + 1) + ' em um ano')


# Exemplo condicionais 1
numero = int(input('Digite um número: '))
if numero > 100:
    print('O número: ' + str(numero) + ' É maior que 100')
else:
    print('O número: ' + str(numero) + ' Não é maior que 100')


# Exemplo condicionais 2
nome = input('Nome: ')
idade = int(input('Idade: '))

if nome == 'João':
    print('Oi, João')
elif idade < 12:
    print('Você não é o João, criança')
elif idade > 2000:
    print('Você não é o João, vampiro importal')
elif idade > 100:
    print('Você não é o João, vovô')


# Exemplo while 1
nome = ''
while nome != 'sair':
    nome = input('Seu nome: ')
    print('Nome informado: ' + nome)
print('Obrigado!')


# Exemplo while 2
nome = ''
while nome != 'sair':
    nome = input('Seu nome: ')
    print('Nome informado: ' + nome)
    if nome == 'João':
        break
print('Obrigado!')


# Exmplo for 1
nome = 'Fulano de Tal Beltrano'
for i in range(5):
    print(nome)


# Exmplo for 2
total = 0
for num in range(101):
    total = total + num
print(total)


# Exmplo for 3
for i in range(0, 10, 2):
    print(i)


# Exemplo funções 1
def hello():
    print('Olá mundo')
    print('Hello world')
    print('Apenas um print')

hello()


# Exemplo funções 2
import random

def bolaMagica(num):
    if num == 1:
        return 'Está certo'
    elif num == 2:
        return 'É decididamente assim'
    elif num == 3:
        return 'Sim'
    elif num == 4:
        return 'Resposta nebulosa, tende novamente'
    elif num == 5:
        return 'Pergunte novamente mais tarde'
    elif num == 6:
        return 'Concentre-se e pergunte novamente'
    elif num == 7:
        return 'Minha resposta é não'
    elif num == 8:
        return 'As perspectivas não tão boas'
    elif num == 9:
        return 'Muito duvidoso'
    
num = random.randint(1, 9)
print(bolaMagica(num))


# Listas
lista = ['gato', 'cachorro', 'camelin', 'rato']
lista.append('leao')
lista.insert(0, 'aaa')

lista.clear()

print(lista)