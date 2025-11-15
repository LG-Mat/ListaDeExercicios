import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def idwr(x, y, z, xnew, ynew):
    n = len(x)
    m = len(xnew)

    znew_idwr = np.zeros(m, dtype=float)

    for j in range(m):
        dist = np.sqrt(np.add(np.power(x - xnew[j], 2), np.power(y - ynew[j], 2)))
        dist[dist == 0] = 1e-10
        w = dist ** (-2)
        s = 1 / np.sum(w)
        ws = w * s
        sumz = np.sum(z)
        den = n ** 2 - np.sum(w) * np.sum(dist ** 2)
        znew_idw = np.sum(np.multiply(ws, z))
        znew_idwr[j] = znew_idw + n * (sumz - n * znew_idw) / den
    return znew_idwr


def idw(x, y, z, xnew, ynew):
    m = len(xnew)

    znew_idw = np.zeros(m, dtype=float)

    for j in range(m):
        dist = np.sqrt(np.add(np.power(x - xnew[j], 2), np.power(y - ynew[j], 2)))
        dist[dist == 0] = 1e-10
        w = dist ** (-2)
        s = 1 / np.sum(w)
        ws = w * s
        znew_idw[j] = np.sum(np.multiply(ws, z))
    return znew_idw

data = pd.read_csv(r'C:\Users\lgmat\PycharmProjects\FundamentosDaCienciaDeDados\ListaDeExercicios\Tarefa09\coal.csv', skiprows=4)
df = data.values
print(data.values[0][1])

x = df[:, 0]
y = df[:, 1]
z = df[:, 2]

N_POINTS = 50

min_x, max_x = x.min(), x.max()
min_y, max_y = y.min(), y.max()

xi = np.linspace(min_x, max_x, N_POINTS)
yi = np.linspace(min_y, max_y, N_POINTS)

X_grid, Y_grid = np.meshgrid(xi, yi)

xnew = X_grid.flatten()
ynew = Y_grid.flatten()

print(f"Grade de interpolação: {N_POINTS}x{N_POINTS} = {len(xnew)} pontos.")

znew_idw = idw(x, y, z, xnew, ynew)

Z_interpolated = znew_idw.reshape((N_POINTS, N_POINTS))

plt.figure(figsize=(10, 8))

im = plt.imshow(Z_interpolated,
                extent=(min_x, max_x, min_y, max_y),
                origin='lower',
                cmap='plasma',
                aspect='auto')

plt.colorbar(im, label='Valor Calorífico')


plt.title('Mapa Interpolado do Valor Calorífico (Método IDW)')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.grid(False)
plt.show()
plt.savefig(r'C:\Users\lgmat\PycharmProjects\FundamentosDaCienciaDeDados\ListaDeExercicios\Tarefa09\HeatMap', dpi=600)
