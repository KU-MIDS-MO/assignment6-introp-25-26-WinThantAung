
import numpy as np

def estimate_pi(num_samples):
    inside_count = 0

    for _ in range(num_samples):
        x = np.random.rand()
        y = np.random.rand()

        if x ** 2 + y ** 2 <= 1:
            inside_count += 1

    pi_estimate = 4 * inside_count / num_samples
    return pi_estimate
