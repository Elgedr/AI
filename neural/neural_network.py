import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from matplotlib.colors import Normalize

if __name__ == '__main__':
    X = np.genfromtxt("happysadpixels.csv", delimiter=",", dtype=int)
    y = np.genfromtxt("happysadlabels.csv", delimiter=",", dtype=int)

    X.shape
    y.shape

    plt.imshow(X[0].reshape(6, 6))
    nn = MLPClassifier(hidden_layer_sizes=(3,), max_iter=2000)
    nn = nn.fit(X, y)
    print("Iterations", nn.n_iter_, "Final loss", nn.loss_)

    weights1 = []
    weights2 = []
    weights3 = []
    norm = Normalize(-1, 1, clip=True)

    for i in range(36):
        weights1.append(nn.coefs_[0][i][0])
        weights2.append(nn.coefs_[0][i][1])
        weights3.append(nn.coefs_[0][i][2])

    # first
    plt.imshow(np.array(weights1).reshape(6, 6), norm=norm)
    plt.show()
    plt.imshow(np.array(weights1 * X[0]).reshape(6, 6), norm=norm)
    plt.show()

    # second
    plt.imshow(np.array(weights2).reshape(6, 6), norm=norm)
    plt.show()
    plt.imshow(np.array(weights2 * X[0]).reshape(6, 6), norm=norm)
    plt.show()

    # third
    plt.imshow(np.array(weights3).reshape(6, 6), norm=norm)
    plt.show()
    plt.imshow(np.array(weights3 * X[0]).reshape(6, 6), norm=norm)
    plt.show()

    out_weights1 = []
    out_weights2 = []

    for j in range(3):
        out_weights1.append(nn.coefs_[1][j][0])
        out_weights2.append(nn.coefs_[1][j][1])

    plt.imshow(np.array(out_weights1).reshape(3, 1))
    plt.show()

    plt.imshow(np.array(out_weights2).reshape(3, 1))
    plt.show()
