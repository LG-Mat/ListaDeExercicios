# -*- coding: utf-8 -*-
"""
Simplified K-Means using NumPy
Created on Wed Apr 20 21:55:03 2022

@author: Leonardo Ramos Emmendorfer
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


def kmeans(x, k):
    n = len(x)

    # Compute the range of min..max values form data
    # minv=np.min(x,0)
    # maxv=np.max(x,0)

    # Generate centroids from randomly selected points

    cent = np.zeros((k, x.shape[1]))
    oldcent = np.copy(cent)

    # for i in range(cent.shape[0]):
    #    for j in range(cent.shape[1]):
    #        cent[i,j]=random.uniform(minv[j],maxv[j])

    selec = (-1) * np.ones((k), dtype=np.uint32)

    oldclus = np.ones((n), dtype=np.uint32)
    clus = np.zeros((n), dtype=np.uint32)
    pos = 0
    while sum(selec == -1) > 0:
        sorteio = random.randrange(n)
        if sum(selec == sorteio) == 0:
            selec[pos] = sorteio
            pos = pos + 1
    for j in range(k):
        cent[j, :] = x[selec[j], :]

    while np.sum(clus - oldclus) > 0:  # np.sum(np.abs(cent-oldcent))>0.1:
        # while the centroids are not stable

        # Compute Euclidean distances to centroids
        dist = np.zeros((n, k))
        for i in range(n):
            for j in range(k):
                dist[i, j] = 0
                for g in range(cent.shape[1]):
                    dist[i, j] = dist[i, j] + (x[i, g] - cent[j, g]) ** 2
                dist[i, j] = np.sqrt(dist[i, j])

        # Determine the centroid closest to each point
        oldclus = np.copy(clus)
        for i in range(n):
            clus[i] = np.round(np.argmin(dist[i, :]))

        # Compute new centroids
        oldcent = np.copy(cent)
        for j in range(k):
            sel = clus == j
            if sum(sel) > 0:
                cent[j, :] = x[clus == j, :].mean(0)

    return (clus)


data = pd.read_csv(r'C:\Users\lgmat\PycharmProjects\FundamentosDaCienciaDeDados\ListaDeExercicios\Tarefa T11\country_cluster.csv')

x = data.iloc[:, 1:3].to_numpy()  # 1t for rows and second for columns

labels = kmeans(x, 3)

plt.scatter(x[:, 0], x[:, 1], c=labels, cmap='rainbow')