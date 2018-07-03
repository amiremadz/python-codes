from sklearn.random_projection import johnson_lindenstrauss_min_dim
import numpy as np
from sklearn import random_projection

# The Johnson-Lindenstrauss lemma
# In mathematics, the Johnson-Lindenstrauss lemma is a result 
# concerning low-distortion embeddings of points from high-dimensional 
# into low-dimensional Euclidean space. The lemma states that a small 
# set of points in a high-dimensional space can be embedded into a space 
# of much lower dimension in such a way that distances between the points
# are nearly preserved. The map used for the embedding is at least Lipschitz, 
# and can even be taken to be an orthogonal projection.
print(johnson_lindenstrauss_min_dim(n_samples=1e6, eps=0.5))
print(johnson_lindenstrauss_min_dim(n_samples=1e6, eps=[0.5, 0.1, 0.01]))
print(johnson_lindenstrauss_min_dim(n_samples=[1e4, 1e5, 1e6], eps=0.1))

# Gaussian random projection
X = np.random.rand(100, 10000)
transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
print(X_new.shape)

# Sparse random projection
X = np.random.rand(100,10000)
transformer = random_projection.SparseRandomProjection()
X_new = transformer.fit_transform(X)
print(X_new.shape)