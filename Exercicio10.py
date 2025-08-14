#  Calcule a idade aproximada de uma pessoa a partir do ano de seu nascimento.
from datetime import datetime

ano_atual = datetime.now().year

ano_nascimento = input('Digite o ano do seu nascimento: ')
ano_nascimento = int(ano_nascimento)

print('Idade aproximada: ', ano_atual - ano_nascimento)