import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

idade = np.array([20, 32, 41, 49, 66])
distancia = np.array([590, 410, 460, 380, 350])

# 1) Calcule o coeficiente de correlação linear de Pearson.
correlacao_pearson, _ = pearsonr(idade, distancia)
print(f"1) Coeficiente de Correlação de Pearson: {correlacao_pearson:.4f}")

# 2) Obtenha um modelo de regressão linear na forma y=a+bx.
b, a = np.polyfit(idade, distancia, 1)
print(f"\n2) Modelo de Regressão Linear: y = {a:.2f} + {b:.2f}x")

# 3) Calcule o valor de distância predito para um motorista com idade de 75 anos.
idade_predicao = 75
distancia_predita = a + b * idade_predicao
print(f"\n3) Distância predita para um motorista com 75 anos: {distancia_predita:.2f} m")

plt.figure(figsize=(10, 6))
plt.scatter(idade, distancia, color='blue', label='Dados Observados')
plt.plot(idade, a + b * idade, color='red', label='Linha de Regressão Linear')
plt.scatter(idade_predicao, distancia_predita, color='green', marker='X', s=100, label=f'Previsão para {idade_predicao} anos')
plt.title('Regressão Linear: Idade vs. Distância de Visão')
plt.xlabel('Idade (anos)')
plt.ylabel('Distância em m (y)')
plt.grid(True)
plt.legend()
plt.show()

plt.savefig(r'C:\Users\lgmat\PycharmProjects\FundamentosDaCienciaDeDados\ListaDeExercicios\Tarefa T10\ImagemPredicao.png', dpi=600)
