import csv
from datetime import datetime

#Exercicio 01 - Leitura do arquivo
def leitura_arquivo():
    with open("actors.csv") as f:
        reader = csv.reader(f)
        next(f) # Exercicio 02 - Remove o cabeçalho
        data = []
        for row in reader:
            data.append(row)
        print(data)

# Exercicio 03
def calcular_idade_media(nome_arquivo):
    total_idade = 0
    contagem_pessoas = 0
    ano_atual = datetime.now().year
    with open(nome_arquivo) as arquivo:
        leitor_csv = csv.reader(arquivo)
        next(leitor_csv)
        for linha in leitor_csv:
            data_aniversario_str = linha[2].strip()
            data_nascimento = datetime.strptime(data_aniversario_str, '%B %d, %Y')
            ano_nascimento = data_nascimento.year
            idade = ano_atual - ano_nascimento
            total_idade += idade
            contagem_pessoas += 1
    media_idade = total_idade / contagem_pessoas
    print("A idade média é de {} anos.".format(media_idade))

nome_do_arquivo = "actors.csv"

leitura_arquivo()
calcular_idade_media(nome_do_arquivo)
