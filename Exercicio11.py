# Calcular a expressão x2+y2/(x-y)2 a partir dos valores x e y dados.

import math
# alteração aqui

x = input('Digite o valor de x: ')
x = float(x)

y = input('Digite o valor de y: ')
y = float(y)

equacao = (pow(x,2)+pow(y,2))/(pow(x-y, 2))

print(equacao)