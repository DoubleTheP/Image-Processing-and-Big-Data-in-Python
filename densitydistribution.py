from sklearn.datasets.samples_generator import make_moons
from sklearn import cluster, datasets
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
import operator
import math
import matplotlib.cm as cm


n_centers = 2
n_samples = 1000

noisy_moons, y = datasets.make_moons(n_samples=n_samples, noise=.05)
#for i in range(2):
	#plt.scatter(noisy_moons[:, 0], noisy_moons[:, 1], color="black")

class Node:
	def __init__(self, content=None, next=None):
		self.content = content
		self.next = next

	def __str__(self):
		return str(self.content)
colors = cm.rainbow(np.linspace(0, 1, n_samples-2))
#Data = [noisy_moons, y];
Data = noisy_moons
start = random.randint(0,9)
Datenliste = []	
for j,c in zip(range(len(Data)-1), colors):
	checklist = []
	for i in range(len(Data)):
	#	for i in [Data for Data in range(100) if Data != start]:
		if i != start:
			checklist.append(np.linalg.norm(Data[i]-Data[start]))
	
	Datenliste.append(Data[start])
	Data = np.delete(Data,start,0)
	start = np.argmin(checklist)
	plt.scatter(Datenliste[j][0],Datenliste[j][1],color=c)
	plt.pause(0.05)


x = []
y = []
for i in range(len(Datenliste)-1):
	x.append(np.linalg.norm(Datenliste[i]-Datenliste[i+1]))
	y.append(i)


for i,c in zip(range(n_samples),colors):
	plt.scatter(Datenliste[i][0],Datenliste[i][1],color=c)
plt.show()
	
	#Data= np.delete(Data,start,0)
	#print(Datenliste)
