from sklearn.datasets.samples_generator import make_blobs
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
import operator
import math

ncenters = 4
nsamples = 1000

X, y = make_blobs(n_samples=nsamples, n_features=2, centers=ncenters, cluster_std=1, random_state=1)


centroids_x = np.random.uniform(low=-10.0, high=10.0, size=(ncenters,))
centroids_y = np.random.uniform(low=-10.0, high=10.0, size=(ncenters,))

plt.scatter(centroids_x, centroids_y, color="black", s=50, label="centroids")	

def kmeans(Data, nsampless, centroids_xx, centroids_yy, centroids_old):
	assignment = np.array([])
	for j in range(nsampless):
		checklist = []
		for i in range(len(centroids_xx)):
			checklist.append(np.linalg.norm(Data[j]-np.array([centroids_xx[i], centroids_yy[i]]))**2)
		if math.isnan(np.argmin(checklist)):
			print("error that should never happen")
		else:
			assignment = np.hstack((assignment, np.argmin(checklist)))

	colors = ["c","yellow","green", "red"]
	for i in range(len(centroids_xx)):
		plt.scatter(Data[assignment == i, 0], Data[assignment == i, 1], color=colors[i], s=10)
	plt.scatter(centroids_xx, centroids_yy, color="black", s=50, label="centroids")	
	plt.show()	


	for i in range(len(centroids_xx)):
		sum = Data[assignment == i].shape[0]
		if sum == 0:
			print("Reseed")
			centroids_xx = random.sample(range(-10,10), ncenters)
			centroids_yy = random.sample(range(-10,10), ncenters)
			return kmeans(Data, nsampless, centroids_xx, centroids_yy, 100.)
		else:
			centroids_xx[i] = np.sum(Data[assignment == i,0])/sum
			centroids_yy[i] = np.sum(Data[assignment == i,1])/sum


	print("Iteration")

	cancel_condition = (np.linalg.norm(centroids_xx) + np.linalg.norm(centroids_yy))
	if float(np.absolute(centroids_old - cancel_condition)) > float(0.0001):
		kmeans(Data, nsampless, centroids_xx, centroids_yy, cancel_condition)
	else:
		return

kmeans(X, nsamples, centroids_x, centroids_y, 100.)