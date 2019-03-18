from sklearn.datasets import make_moons
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random


epsilon = 0.075
minPoint = 5
n_samples = 1000

noisy_moons, y = make_moons(n_samples=n_samples, noise=.05)

colors = cm.rainbow(np.linspace(0, 1, n_samples-2))
checked = np.zeros((n_samples, 1), bool)
cluster_number = np.zeros((n_samples, 1), dtype=np.int)
assigned = np.zeros((n_samples, 1), dtype=np.int)
Data = np.concatenate((noisy_moons, checked, cluster_number, assigned), axis=1)


start = random.randint(0,n_samples-1)


k = [1]
while len(k) != 0:
    checklist = []
    for i in range(len(Data)):
        if np.linalg.norm(Data[i][:2]-Data[start][:2]) <= epsilon:
            checklist.append([np.linalg.norm(Data[i][:2]-Data[start][:2]),i])
            Data[i][3] = 1
    Data[start][2] = True
    if len(checklist) >= minPoint:#core
       Data[start][4] = "1"
    elif len(checklist) == 0:
        Data[start][4] = "3" #outline
    else:
        Data[start][4] = "2" #border

    k = []
    for i in range(len(Data)):
        if Data[i][3] == 1 and Data[i][2] == False:
            k.append(i)
            start = i



for i in range(len(Data)):
    if Data[i][4] == 1:
    	plt.scatter(Data[i][0], Data[i][1], c="green", s=10)
    elif Data[i][4] == 2:
    	plt.scatter(Data[i][0], Data[i][1], c="red", s=10)
    else:
        plt.scatter(Data[i][0], Data[i][1], facecolors='none', edgecolors="black", s=10)

plt.show()
