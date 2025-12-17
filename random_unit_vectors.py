import numpy as np

def random_unit_vectors(num_vectors, dim):

    M = np.random.randn(num_vectors, dim)

    norms = np.linalg.norm(M, axis=1)

    M_unit = M / norms[:, np.newaxis]

    return M_unit

