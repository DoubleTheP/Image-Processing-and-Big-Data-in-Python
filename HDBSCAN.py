from sklearn.datasets.samples_generator import make_blobs
from sklearn.datasets import make_moons
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

n_Samples = 300
n_Noise = 100
n_Points = 20
n_Centers = 2

X, y = make_blobs(n_samples=n_Samples, n_features=2, centers=n_Centers, cluster_std=1, random_state=1)
X, y = make_moons(n_samples=n_Samples, noise=.05)
checked = (np.random.rand(n_Noise,2)-0.5)*5
X = np.concatenate((X, checked), axis=0)


n_Samples = n_Samples + n_Noise


checked = np.zeros((n_Samples, 1), dtype=np.int)
from_To = np.zeros((n_Samples, 2*(n_Samples-1)), dtype=np.float) #(index, distance)*5
density = np.zeros((n_Samples, 1), dtype=np.float)
data = np.concatenate((X, checked, from_To, density), axis=1)


for start in range(n_Samples):
    checklist = []
    for i in range(n_Samples):
        checklist.append(np.linalg.norm(data[i][:2]-data[start][:2]))

    checklist = list(sorted(enumerate(checklist), key=lambda x:x[1]))

    for i in range(1,n_Samples):
        data_Input = list(checklist[i])
        data[start][3+2*(i-1)] = data_Input[0]
        data[start][3+2*i-1] = data_Input[1]


for zae in range(n_Samples):
    for j in range(n_Samples-1):
        if zae in (data[int(data[zae][3+2*j])][3:3+n_Points*2]) and ((data[zae][3+2*j]) in data[zae][3:3+n_Points*2]):
            data[zae][-1] = data[zae][-1] + data[zae][3+2*j+1]
        elif (data[zae][3+2*j]) in data[zae][3:3+n_Points*2]:
            data[zae][-1] = data[zae][-1] + data[zae][3+2*n_Points+1]
        elif (data[zae][3+2*j+1]) < (data[zae][3+2*n_Points+1] + data[int(data[zae][3+2*(j-1)])][3+2*n_Points+1]):
            data[zae][-1] = data[zae][-1] + data[zae][3+2*j+1]



cm = cm.get_cmap('RdYlBu')

colors = []
X = []
Y = []
for i in range(n_Samples):
    colors.append(data[i][-1])
    X.append(data[i][0])
    Y.append(data[i][1])
minColor = min(colors)
maxColor = max(colors)

plt.scatter(X, Y, c=colors, vmin=minColor, vmax=maxColor, s=35, cmap=cm)
plt.colorbar()
plt.show()

for i in range(n_Samples):
    if data[i][-1] > 40:
        plt.scatter(X[i], Y[i], facecolors='none', edgecolors='b')
    else:
        plt.scatter(X[i], Y[i], facecolors='none', edgecolors='r')
plt.show()