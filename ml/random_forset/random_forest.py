from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV

from sklearn import metrics

from matplotlib import pyplot as plt

from utils import visualize_classifier

import seaborn as sns
import numpy as np
import sys

######## regression #########

rng = np.random.RandomState(42)

x = 10 * rng.rand(200)

def model(x, sigma=0.3):
    fast_oscillation = np.sin(5 * x)
    slow_oscillation = np.sin(0.5 * x)

    noise = sigma * rng.randn(len(x))

    return slow_oscillation + fast_oscillation + noise

y = model(x)

print(x.shape, y.shape)

regforest = RandomForestRegressor(200)
regforest.fit(x[:, None], y)

print(regforest.get_params())

xfit = np.linspace(0, 10, 1000)
yfit = regforest.predict(xfit[:, None])
ytrue = model(xfit, sigma=0)

plt.figure()
plt.errorbar(x, y, 0.3, fmt='o', alpha=0.5)
plt.plot(xfit, yfit, '-r', label='fit')
plt.plot(xfit, ytrue, '-k', alpha=1, label='gt')
plt.legend()
plt.title('a random model performance')

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
print(random_grid)

# Use the random grid to search for best hyperparameters
# First create the base model to tune
rf = RandomForestRegressor()
# Random search of parameters, using 3 fold cross validation, 
# search across 100 different combinations, and use all available cores
random_search = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)
# Fit the random search model
random_search.fit(x[:, None], y)

print(random_search.best_params_)

best_random = random_search.best_estimator_
yfit_rnd = best_random.predict(xfit[:, None])

plt.figure()
plt.errorbar(x, y, 0.3, fmt='o', alpha=0.5)
plt.plot(xfit, yfit_rnd, '-r', label='fit')
plt.plot(xfit, ytrue, '-k', alpha=1, label='gt')
plt.legend()
plt.title('optimized model parameters')

if 0:
    # Create the parameter grid based on the results of random search 
    param_grid = {
        'bootstrap': [True],
        'max_depth': [80, 90, 100, 110],
        'max_features': [2, 3],
        'min_samples_leaf': [3, 4, 5],
        'min_samples_split': [8, 10, 12],
        'n_estimators': [100, 200, 300, 1000]
    }
    # Create a based model
    rf_reg = RandomForestRegressor()
    # Instantiate the grid search model
    grid_search = GridSearchCV(estimator = rf_reg, param_grid = param_grid, 
                              cv = 3, n_jobs = -1, verbose = 2)

    grid_search.fit(x[:, None], y)

    print(grid_search.best_params_)

    best_grid = grid_search.best_estimator_
    yfit_grid = best_grid.predict(xfit[:, None])

    plt.figure()
    plt.errorbar(x, y, 0.3, fmt='o', alpha=0.5)
    plt.plot(xfit, yfit_grid, '-r', label='fit')
    plt.plot(xfit, ytrue, '-k', alpha=1, label='gt')
    plt.legend()

######### image classification ###########

digits = load_digits()
print(digits.keys())

fig = plt.figure(figsize=(6,6))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

for i in range(64):
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    
    # 8x8 images
    img = digits.images[i]
    ax.imshow(img, cmap=plt.cm.binary, interpolation='nearest')

    ax.text(0, 7, str(digits.target[i]))

Xtrain, Xtest, ytrain, ytest = train_test_split(digits.data, digits.target, random_state=0)

print(Xtrain.shape)
print(ytrain.shape)

classforest = RandomForestClassifier(n_estimators=1000)
classforest.fit(Xtrain, ytrain)

print(classforest.get_params())

ypred = classforest.predict(Xtest)

print(metrics.classification_report(ypred, ytest))

confmat = metrics.confusion_matrix(ytest, ypred)

plt.figure()
sns.heatmap(confmat.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label')

plt.show()
