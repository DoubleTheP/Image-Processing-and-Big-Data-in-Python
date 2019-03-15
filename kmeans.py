from sklearn.datasets.samples_generator import make_blobs
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
import operator
import math

ncenters = 3
nsamples = 100

X, y = make_blobs(n_samples=nsamples, n_features=2, centers=ncenters, cluster_std=0.6, random_state=1)




x = np.arange(10)
ys = [i+x+(i*x)**2 for i in range(100)]
colors = cm.rainbow(np.linspace(0, 1, len(ys)))

centroids_x = random.sample(range(-5,5), ncenters)
centroids_y = random.sample(range(-5,5), ncenters)
print(centroids_x,centroids_y)
plt.scatter(centroids_x, centroids_y, color="black", s=50, label="centroids")	

#plt.scatter(centroids_x, centroids_y, color="black", s=10, label="centroids")

def kmeans(Data, nsampless, centroids_xx, centroids_yy, centroids_old):
	assignment = np.array([])
	for j in range(nsampless):
		checklist = []
		for i in range(len(centroids_xx)):
			checklist.append(np.linalg.norm(Data[j]-np.array([centroids_xx[i], centroids_yy[i]])))
		if math.isnan(np.argmin(checklist)):
			print(np.argmin(checklist))
		else:
			assignment = np.hstack((assignment, np.argmin(checklist)))

	#print(centroids_xx, centroids_yy)
	for i in range(len(centroids_xx)):
		sum = Data[assignment == i].shape[0]
		centroids_xx[i] = np.sum(Data[assignment == i,0])/sum
		centroids_yy[i] = np.sum(Data[assignment == i,1])/sum
	#print(centroids_xx, centroids_yy)


	print("Iteration ")

	cancel_condition = (np.linalg.norm(centroids_xx) + np.linalg.norm(centroids_yy))
	print(cancel_condition, centroids_old)
	if float(np.absolute(centroids_old - cancel_condition)) > float(0.0001):
		kmeans(Data, nsampless, centroids_xx, centroids_yy, cancel_condition)
	else:
		print(centroids_xx, centroids_yy)
		colors = ["c","yellow","green"]
		for i in range(len(centroids_xx)):
			plt.scatter(X[y == i, 0], X[y == i, 1], color=colors[i], s=10)
		#plt.scatter(X[y == 1, 0], X[y == 1, 1], color="blue", s=10, label="Cluster2")
		#plt.scatter(X[y == 2, 0], X[y == 2, 1], color="green", s=10, label="Cluster3")
		plt.scatter(centroids_xx, centroids_yy, color="red", s=50, label="centroids")	
		return plt.show()


kmeans(X, nsamples, centroids_x, centroids_y, 100.)