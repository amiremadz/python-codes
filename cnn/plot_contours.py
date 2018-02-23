from matplotlib import pyplot as plt

def make_meshgrid(x, y, h=.02):
    """Create a mesh of points to plot in

    Parameters
    ----------
    x: data to base x-axis meshgrid on
    y: data to base y-axis meshgrid on
    h: stepsize for meshgrid, optional

    Returns
    -------
    xx, yy : ndarray
    """
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy

def plot_contours(ax, Z, xx, yy, **params):
    """Plot the decision boundaries for a classifier.

    Parameters
    ----------
    ax: matplotlib axes object
    clf: a classifier
    xx: meshgrid ndarray
    yy: meshgrid ndarray
    params: dictionary of params to pass to contourf, optional
    """
    #Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

# Generating some data
N = 100 # number of points per class
D = 2 # dimensionality
K = 3 # number of classes
X = np.zeros((N*K,D)) # data matrix (each row = single example)
y = np.zeros(N*K, dtype='uint8') # class labels

X0, X1 = X[:, 0], X[:, 1]
xx, yy = make_meshgrid(X0, X1)

X_all = np.c_[xx.ravel(), yy.ravel()]
scores_all_smax = np.dot(X_all, W) + b
Z_smax = np.argmax(scores_all_smax, axis=1)

title = "Linear softmax classifier"
fig, ax = plt.subplots(1, 1)
plot_contours(ax, Z_smax, xx, yy,
                  cmap=plt.cm.Spectral, alpha=0.8) # cmap=plt.cm.coolwarm
ax.scatter(X0, X1, c=y, cmap=plt.cm.Spectral, s=40, edgecolors='k')
ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())
ax.set_xlabel('$x_0$')
ax.set_ylabel('$x_1$')
ax.set_xticks(())
ax.set_yticks(())
ax.set_title(title)

plt.show()