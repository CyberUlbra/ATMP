import csv
from email.message import Message
import smtplib

lista_amigos = []
corpo_email = open('index.html', 'r', encoding='utf-8').read()

def recuperarEmail(nome_arquivo):
    arquivo = open(nome_arquivo)
    linhas = csv.reader(arquivo)

    for linha in linhas:
        lista_amigos.append(linha)
    
    lista_amigos.pop(0)


def enviar_email_smtp(corpo_email_envio, email_to):
    mensagem = Message()
    mensagem['Subject'] = "Pagamento Netflix"
    mensagem['From'] = 'minicursoatmp@gmail.com'
    mensagem['To'] = email_to
    password = 'senha' 
    mensagem.add_header('Content-Type', 'text/html')
    mensagem.set_payload(corpo_email_envio)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login
    s.login(mensagem['From'], password)
    s.sendmail(mensagem['From'], [mensagem['To']], mensagem.as_string().encode('utf-8'))
    print('Email enviado')


def enviar_email():
    for i in lista_amigos:
        amigo_cobrado = i[0].replace(';', ',').split(',')
        paragrafo = '<p>Nome: {} | Valor: {}</p>'
        
        corpo = corpo_email.replace('amigues_cobranca', paragrafo.format(amigo_cobrado[1], amigo_cobrado[2]))
        
        enviar_email_smtp(corpo, amigo_cobrado[3])


nome_arquivo = input('Qual o nome do arquivo: ')
recuperarEmail(nome_arquivo)
enviar_email()
