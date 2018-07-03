import numpy as np

# A/B testing

num_samples  = 10000

num_clicks_A = 200
num_views_A  = 5000

num_clicks_B = 230
num_views_B  = 6000

A = np.random.beta(1 + num_clicks_A, 1 + num_views_A - num_clicks_A, size = num_samples)
B = np.random.beta(1 + num_clicks_B, 1 + num_views_B - num_clicks_B, size = num_samples)

# Probabilty thta A wins
print(np.sum(A > B) / float(num_samples))

# Probabilty thta A > B + 1%
print(np.sum(A > (B + 0.01)) / float(num_samples))