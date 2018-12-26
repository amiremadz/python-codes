import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging

from scipy import stats

from sklearn.svm import SVC
from sklearn.datasets.samples_generator import make_blobs

from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV

sns.set()
logging.basicConfig(level=logging.INFO)

# create data
X, y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std = 0.6)

plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.xlim(-1, 3.5)

xfit = np.linspace(-1, 3.5)

plt.plot([0.6], [2.1], 'x', color='red', markeredgewidth=2, markersize=10)

for m, b, d in [(1, .65, .33), (.5, 1.6, .55), (-.2, 2.9, .2)]:
    yfit =  m * xfit + b
    plt.plot(xfit, yfit, '-k')
    plt.fill_between(xfit, yfit -d, yfit + d, edgecolor='none', color='#AAAAAA', alpha=.4)

model = SVC(kernel='linear', C=1e10)
model.fit(X, y)

print(model.support_vectors_)
print(model.get_params(deep=True))

# get the separating hyperplane
# y = m * x + b

w = model.coef_[0]
m = -w[0] / w[1]
b = -model.intercept_[0] / w[1] 

print(model.coef_)
print(model.intercept_)

def plot_svc_decision_function(model, ax=None, plot_support=True):
    if ax is None:
        ax = plt.gca()

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # create grid to evaluate model
    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y, X = np.meshgrid(y, x)
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    logging.info(xy.shape)
    P = model.decision_function(xy).reshape(X.shape)

    # plot decision boundary and margins
    ax.contour(X, Y, P, colors='k',
               levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'])
    
    # plot support vectors
    if plot_support:
        ax.scatter(model.support_vectors_[:, 0],
                   model.support_vectors_[:, 1],
                   s=300, linewidth=1, facecolor='none', edgecolor='k')
    
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

plt.figure()
ax = plt.gca()
xx = np.linspace(-5, 5)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
plot_svc_decision_function(model)
plt.plot(xx, m * xx + b, linestyle='-.', linewidth=5, alpha=0.6)

def plot_svm(N=10, ax=None):
    X, y = make_blobs(n_samples=200, centers=2, random_state=0, cluster_std=0.6)
    X = X[:N]
    y = y[:N]

    model = SVC(kernel='linear', C=1e10)
    model.fit(X, y)
    print(model.coef_)
    print(model.intercept_)

    ax = ax or plt.gca()
    ax.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 6)
    plot_svc_decision_function(model, ax)

# only the position og=f SVs matter; any points further
# from the margin which are on the correct side do not
# modify the fit
fig, ax = plt.subplots(1, 2, figsize=(16, 6))
fig.subplots_adjust(left=.0625, right=.95, wspace=.1)
for axi, N in zip(ax, [60, 120]):
    plot_svm(N, axi)
    axi.set_title('N = {0}'.format(N))

# Grid search
param_grid = [
  {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
  {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
 ]

model = SVC()

grid_search = GridSearchCV(estimator = model, param_grid = param_grid, 
                          cv = 3, n_jobs = -1, verbose = 2)

grid_search.fit(X, y)

print(grid_search.best_params_)
print(grid_search.best_estimator_)
print(grid_search.cv_results_)





plt.show()

