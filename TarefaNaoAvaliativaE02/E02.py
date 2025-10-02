# Em uma fábrica, a máquina X produz 35% do total da produção; a máquina Y, 40% e a máquina Z os restantes 25%.
# Da produção de X, 2% apresentam defeito; da produção de Y, 1,5% apresentam defeito, e da produção de Z, 0,8% apresentam defeito.
# Em um dia em que a produção total das 3 máquinas foi de 20.000 peças,
# uma delas foi tirada ao acaso e verificou-se que era defeituosa.
# Qual a probabilidade de que essa peça tenha sido produzida pela máquina X?

producao_total = 20000

porcao_X = 0.35
porcao_Y = 0.4
porcao_Z = 0.25

defeitos_X = 0.02
defeitos_Y = 0.015
defeitos_Z = 0.008

producao_X = producao_total * porcao_X
producao_Y = producao_total * porcao_Y
producao_Z = producao_total * porcao_Z

print(producao_X, producao_Y, producao_Z)

prod_defeito_X = producao_X * defeitos_X
prod_defeito_Y = producao_Y * defeitos_Y
prod_defeito_Z = producao_Z * defeitos_Z

print(prod_defeito_X, prod_defeito_Y, prod_defeito_Z)

prod_defeito_total = prod_defeito_X + prod_defeito_Y + prod_defeito_Z

print(prod_defeito_total)

prob_X = prod_defeito_X / prod_defeito_total

print(prob_X)

# A probabilidade de ser uma peça produzida pela máquina X é de 46.6%
