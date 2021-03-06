from sklearn.datasets import make_moons
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random


epsilon = 0.075
minPoint = 5
n_samples = 1000

n_centers = 4

X, y = make_blobs(n_samples=n_samples, n_features=2, centers=n_centers, cluster_std=1, random_state=1)
#noisy_moons, y = make_moons(n_samples=n_samples, noise=.05)

checked = np.zeros((n_samples, 1), bool)
cluster_number = np.zeros((n_samples, 1), dtype=np.int)
assigned = np.zeros((n_samples, 1), dtype=np.int)
Data = np.concatenate((noisy_moons, checked, cluster_number, assigned), axis=1)


start = random.randint(0,n_samples-1)
cluster_no = 1



def detect_densities(start, cluster_no, Data):
    k = [1]
    while len(k) != 0:
        checklist = []
        for i in range(len(Data)):
            if np.linalg.norm(Data[i][:2]-Data[start][:2]) <= epsilon:
                checklist.append([np.linalg.norm(Data[i][:2]-Data[start][:2]),i])
                Data[i][3] = cluster_no
        Data[start][2] = True
        if len(checklist) >= minPoint:#core
           Data[start][4] = "1"
        elif len(checklist) == 0:
            Data[start][4] = "3" #outline
        else:
            Data[start][4] = "2" #border

        k = []
        zae = 0
        for i in range(len(Data)):
            if Data[i][2] == True:
                zae += 1
            if Data[i][3] == cluster_no and Data[i][2] == False:
                k.append(i)
                start = i
    print(zae)

    if zae != n_samples:
        for i in range(len(Data)):
            if Data[i][3] == False:
                start = i
                cluster_no += 1
                return detect_densities(start, cluster_no, Data)
    else:
        return

detect_densities(start, cluster_no, Data)

print(cluster_no)



for i in range(len(Data)):
    if Data[i][3] == 1:
    	plt.scatter(Data[i][0], Data[i][1], c="green", s=10)
    elif Data[i][3] == 2:
    	plt.scatter(Data[i][0], Data[i][1], c="red", s=10)
    else:
        plt.scatter(Data[i][0], Data[i][1], facecolors='none', edgecolors="black", s=10)

plt.show()
