import numpy as np


def mesh_exp(r_min, r_max, a, N):
    """Creates an exponential radial mesh.

    """
    mesh = np.zeros(N+1)
    beta = np.log(a) / (N-1)
    alpha = (r_max - r_min) / (np.exp(beta*N) - 1)
    for i in range(0, N+1):
        mesh[i] = alpha * (np.exp(beta*(i)) - 1) + r_min
    return mesh
