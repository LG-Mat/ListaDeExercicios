import numpy as np
import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv(r'/ListaDeExercicios/Classificadores/sample_data.csv')

train, test = train_test_split(df, test_size = 0.25)

train_x = train[['Weight', 'Size']]
train_y = train['Class']

test_x = test[['Weight', 'Size']]
test_y = test['Class']

train_x.head(2)

model = svm.SVC(kernel = 'linear', C = 1)
model.fit(train_x, train_y)
prediction = model.predict(test_x)

print(prediction)

print('Precisão: {}'.format(metrics.accuracy_score(prediction, test_y)))
print('Acurácia: {}'.format(metrics.precision_score(test_y, prediction, average = 'weighted')))
print('Recall: {}'.format(metrics.recall_score(test_y, prediction, pos_label = 'apple')))
print('F1-Score: {}'.format(metrics.f1_score(test_y, prediction, pos_label = 'apple')))

graph = train[train.Class == 'orange'].plot(kind = 'scatter', x='Weight', y='Size', color = 'orange')
train[train.Class == 'apple'].plot(kind = 'scatter', x='Weight', y='Size', color = 'red', ax=graph)

linhas = plt.gca()
xlim = linhas.get_xlim()
ylim = linhas.get_ylim()

xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T

Z = model.decision_function(xy).reshape(XX.shape)

linhas.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
linhas.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=100, linewidth=1, facecolors='none', edgecolors='blue')

graph.set_xlabel('Size')
graph.set_ylabel('Weight')
graph.set_title('Classificação de maçãs e laranjas')
graph = plt.gcf()
graph.set_size_inches(8, 5)

plt.show()
