from sklearn.datasets.samples_generator import make_blobs
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random


epsilon = 0.075

n_Samples = 10
n_Points = 5
n_Centers = 4

X, y = make_blobs(n_samples=n_Samples, n_features=2, centers=n_Centers, cluster_std=1, random_state=1)

checked = np.zeros((n_Samples, 1), dtype=np.int)
from_To = np.zeros((n_Samples, 2*n_Points), dtype=np.float) #(index, distance)*5
data = np.concatenate((X, checked, from_To), axis=1)


for start in range(n_Samples):
    checklist = []
    for i in range(n_Samples):
        checklist.append(np.linalg.norm(data[i][:2]-data[start][:2]))

    checklist = list(sorted(enumerate(checklist), key=lambda x:x[1]))

    for i in range(1,n_Points+1):
        data_Input = list(checklist[i])
        data[start][3+2*(i-1)] = data_Input[0]
        data[start][3+2*i-1] = data_Input[1]

print(data)
if 7 in data[start][3:]:
    print("yes")



#if np.linalg.norm(data[i][:2]-data[start][:2]) <= epsilon: