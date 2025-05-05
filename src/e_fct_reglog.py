import numpy as np
from scipy.linalg import eigh


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def norm(x):
    return np.max(np.abs(x))


def gradient_logistic_regression(X, y, w):
    return (np.array((sigmoid(X @ w) - y)).reshape(-1, 1) * X).mean(axis=0)


def lr_opti(X):
    lr = (4 * X.shape[0]) / eigh(
        X.T @ X,
        eigvals_only=True,
        subset_by_index=[X.shape[1] - 1, X.shape[1] - 1]
    ).item()
    return lr


def gradient_descent(X, y, max_iter, tol, lr):
    w = np.zeros(X.shape[1])
    grad = gradient_logistic_regression(X, y, w)
    if norm(grad) < tol:
        return {'coef': w, 'convergé': True, 'n_iter': 0}
    converge = False
    for n_iter in range(1, max_iter + 1):
        w -= lr * grad
        grad = gradient_logistic_regression(X, y, w)
        if norm(grad) < tol:
            converge = True
            break
    return {'coef': w, 'convergé': converge, 'n_iter': n_iter, 'gradient': grad}


def prediction(x, w):
    return x@w > 0
